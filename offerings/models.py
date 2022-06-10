from datetime import tzinfo

from django.db import models

# Create your models here.
from church_services.models import ChurchService


class OfferingType(models.Model):
    type_of_offering = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.type_of_offering


class Offering(models.Model):
    service = models.ForeignKey(ChurchService, on_delete=models.CASCADE)
    type_of_offering = models.ForeignKey(OfferingType, on_delete=models.CASCADE)
    amount = models.FloatField(null=False, blank=False, default=0.00)
    notes = models.TextField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service} - {self.amount}"