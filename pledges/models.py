from django.db import models

# Create your models here.
from membership.models import Member


class Pledge(models.Model):
    redeemed_status_choices = (
        ('pending', 'Pending'),
        ('redeemed', 'Redeemed'),
    )
    pledge_person = models.CharField(max_length=255, blank=False, null=False)
    # contact_information = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=255, blank=True, null=True)

    redeemed_status = models.CharField(max_length=255, blank=False, null=False, choices=redeemed_status_choices,
                                       default=redeemed_status_choices[0][0])

    item = models.CharField(max_length=255, blank=False, null=False)
    quantity_pledged = models.IntegerField(null=False, blank=False, default=0)
    quantity_redeemed = models.IntegerField(null=True, blank=True, default=0)
    description = models.TextField(blank=True, null=True)

    amount_paid = models.FloatField(null=True, blank=True, default=0.00)
    amount_pledged = models.FloatField(null=False, blank=False, default=0.00)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.person} – {self.redeemed_status.capitalize()}"

    def save(self, *args, **kwargs):
        if self.amount_pledged and self.amount_paid:
            if self.amount_paid >= self.amount_pledged:
                self.redeemed_status = self.redeemed_status_choices[1][0]
            else:
                self.redeemed_status = self.redeemed_status_choices[0][0]

        if self.quantity_pledged and self.quantity_redeemed:
            if self.quantity_pledged <= self.quantity_redeemed:
                self.redeemed_status = self.redeemed_status_choices[1][0]
            else:
                self.redeemed_status = self.redeemed_status_choices[0][0]

        super().save(*args, **kwargs)


class MonetaryPledge(Pledge):
    item = None
    quantity_pledged = None
    quantity_redeemed = None
    contact_information = None
    # description = None


class ItemPledge(Pledge):
    item = models.CharField(max_length=255, blank=False, null=False)
    amount_pledged = None
    amount_paid = None


class MemberMonetaryPledge(Pledge):
    pledge_person = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    item = None
    quantity_pledged = None
    quantity_redeemed = None
    description = None
    contact_information = None
    person = None


class MemberItemPledge(Pledge):
    pledge_person = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    item = models.CharField(max_length=255, blank=False, null=False)
    amount_pledged = None
    amount_paid = None