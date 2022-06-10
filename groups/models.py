from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    description = models.TextField(null=True, blank=True)

    # president = models.OneToOneField(Member, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name