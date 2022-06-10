from django.db import models


# Create your models here.
class ChurchEvent(models.Model):
    types = (
        ('one-time', 'One-Time'),
        ('recurring', 'Recurring'),
    )
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, null=False, blank=False)
    start_date = models.DateTimeField(max_length=255, null=False, blank=False)
    end_date = models.DateTimeField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=20, choices=types, default=None)
    email_recipients = models.BooleanField(default=False)

    def __str__(self):
        return self.title