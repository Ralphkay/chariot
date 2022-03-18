from django.contrib import admin

# Register your models here.
from pledges.models import MonetaryPledge, MaterialPledge, MemberMonetaryPledge, MemberMaterialPledge


class MonetaryPledgeAdmin(admin.ModelAdmin):
    readonly_fields = ['redeemed_status']


admin.site.register(MonetaryPledge, MonetaryPledgeAdmin)


class MaterialPledgeAdmin(admin.ModelAdmin):
    readonly_fields = ['redeemed_status']


admin.site.register(MaterialPledge, MaterialPledgeAdmin)


class MemberMaterialPledgeAdmin(admin.ModelAdmin):
    readonly_fields = ['redeemed_status']


class MemberMaterialPledgeAdmin(admin.ModelAdmin):
    readonly_fields = ['redeemed_status']


admin.site.register(MemberMonetaryPledge, MemberMaterialPledgeAdmin)
admin.site.register(MemberMaterialPledge, MemberMaterialPledgeAdmin)
