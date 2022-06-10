from django.contrib import admin

# Register your models here.
from accounts.models import User, ActivateUser

admin.site.register(User)
admin.site.register(ActivateUser)