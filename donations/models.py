from django.db import models

# Create your models here.
from membership.models import Member


class MonetaryDonation(models.Model):
    payment_methods = (
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
        ('mobile_money', 'Mobile Money'),
    )

    description = models.TextField(blank=True, null=True)
    amount_donated = models.FloatField(null=False, blank=False, default=0.00)
    payment_method = models.CharField(max_length=255, blank=False, null=False, choices=payment_methods, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExternalMonetaryDonation(MonetaryDonation):
    donor = models.CharField(max_length=255, blank=False, null=False)


class MemberMonetaryDonation(MonetaryDonation):
    donor = models.ForeignKey(Member, on_delete=models.CASCADE)


class MaterialDonation(models.Model):
    item = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.IntegerField(null=False, blank=True, default=0)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExternalMaterialDonation(MaterialDonation):
    donor = models.CharField(max_length=255, blank=False, null=False)


class MemberMaterialDonation(MaterialDonation):
    donor = models.ForeignKey(Member, on_delete=models.CASCADE)
