from django.contrib import admin

# Register your models here.
from welfare.models import Welfare, WelfareContribution, WelfareMembershipLevy

admin.site.register(Welfare)
admin.site.register(WelfareContribution)
admin.site.register(WelfareMembershipLevy)