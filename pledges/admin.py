from django.contrib import admin

# Register your models here.
from pledges.models import MonetaryPledge, ItemPledge, MemberMonetaryPledge, MemberItemPledge


class MonetaryPledgeAdmin(admin.ModelAdmin):
    readonly_fields = ['redeemed_status']


admin.site.register(MonetaryPledge, MonetaryPledgeAdmin)


class ItemPledgeAdmin(admin.ModelAdmin):
    readonly_fields = ['redeemed_status']


admin.site.register(ItemPledge, ItemPledgeAdmin)


class MemberItemPledgeAdmin(admin.ModelAdmin):
    readonly_fields = ['redeemed_status']


class MemberItemPledgeAdmin(admin.ModelAdmin):
    readonly_fields = ['redeemed_status']


admin.site.register(MemberMonetaryPledge, MemberItemPledgeAdmin)
admin.site.register(MemberItemPledge, MemberItemPledgeAdmin)