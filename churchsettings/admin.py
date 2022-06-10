from django.contrib import admin

# Register your models here.
from churchsettings.models import ChurchSettings, ChurchSetup

admin.site.register(ChurchSetup)
admin.site.register(ChurchSettings)