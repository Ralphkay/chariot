from django.db import models

# Create your models here.
from churchclicks import settings


class ChurchSetup(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    church_name = models.CharField(max_length=255, null=False, blank=False)
    short_name = models.CharField(max_length=12, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # description = models.TextField(null=True, blank=True)

    # location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.church_name


class ChurchSettings(models.Model):
    church = models.ForeignKey(ChurchSetup, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.church