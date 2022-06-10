from django.db import models


# Create your models here.

class Expense(models.Model):
    item = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    amount = models.FloatField(null=False, blank=False, default=0.00)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item}"