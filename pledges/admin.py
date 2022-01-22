from django.contrib import admin

# Register your models here.
from pledges.models import MonetaryPledge, MaterialPledge, MemberMonetaryPledge, MemberMaterialPledge

admin.site.register(MonetaryPledge)
admin.site.register(MaterialPledge)
admin.site.register(MemberMonetaryPledge)
admin.site.register(MemberMaterialPledge)