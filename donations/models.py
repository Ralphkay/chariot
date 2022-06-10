from django.db import models

# Create your models here.
from membership.models import Member


class Donation(models.Model):
    donor = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=255, blank=True, null=True)
    item = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    amount = models.FloatField(null=False, blank=False, default=0.00)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.donor}"


class MonetaryDonation(Donation):
    item = None
    quantity_pledged = None
    quantity = None


class MemberMonetaryDonation(models.Model):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    amount = models.FloatField(null=False, blank=False, default=0.00)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_on', 'updated_on')


class MemberItemDonation(models.Model):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    item = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.IntegerField(null=False, blank=True, default=0)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_on', 'updated_on')