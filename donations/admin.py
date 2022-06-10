from django.contrib import admin

# Register your models here.
from donations.models import MemberMonetaryDonation, MemberItemDonation

admin.site.register(MemberMonetaryDonation)
admin.site.register(MemberItemDonation)