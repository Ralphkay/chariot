from django.contrib import admin

# Register your models here.
from donations.models import MemberMonetaryDonation, MemberMaterialDonation,ExternalMonetaryDonation,ExternalMaterialDonation

admin.site.register(MemberMonetaryDonation)
admin.site.register(MemberMaterialDonation)
admin.site.register(ExternalMonetaryDonation)
admin.site.register(ExternalMaterialDonation)