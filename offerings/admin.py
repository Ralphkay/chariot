from django.contrib import admin

# Register your models here.
from offerings.models import Offering, OfferingType

admin.site.register(Offering)
admin.site.register(OfferingType)