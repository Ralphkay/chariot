from django.contrib import admin

# Register your models here.
from membership.models import Member, MemberReligiousCV


class MemberAdmin(admin.ModelAdmin):
    list_display = ('fullname','occupation','residential_address','created_on', 'updated_on')


admin.site.register(Member, MemberAdmin)
admin.site.register(MemberReligiousCV)