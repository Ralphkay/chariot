from django.db import models


# Create your models here.

class ChurchService(models.Model):
    title = models.CharField(max_length=255)
    # start_time = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title