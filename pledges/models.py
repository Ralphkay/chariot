from django.db import models

# Create your models here.
from membership.models import Member


class Pledge(models.Model):
    redeemed_status_choices = (
        ('pending', 'Pending'),
        ('redeemed', 'Redeemed'),
    )

    pledge_person = models.CharField(max_length=255, blank=False, null=False)

    redeemed_status = models.CharField(max_length=255, blank=False, null=False, choices=redeemed_status_choices,
                                       default=redeemed_status_choices[0])
    amount_pledge = models.FloatField(null=False, blank=False, default=0.00)

    contact_information = models.TextField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.pledge_person} – {self.redeemed_status.capitalize()}"


class MonetaryPledge(Pledge):
    amount_pledge = models.FloatField(null=False, blank=False, default=0.00)


class MaterialPledge(Pledge):
    item = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.IntegerField(null=False, blank=True, default=0)
    description = models.TextField(blank=True, null=True)
    amount_pledge = None


class MemberMonetaryPledge(Pledge):
    pledge_person = models.ForeignKey(Member, on_delete=models.CASCADE)


class MemberMaterialPledge(Pledge):
    pledge_person = models.ForeignKey(Member, on_delete=models.CASCADE)

    item = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.IntegerField(null=False, blank=True, default=0)
    description = models.TextField(blank=True, null=True)
