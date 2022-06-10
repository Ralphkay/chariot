from django.urls import path, include

from churchsettings.views import setup_church,church_settings

urlpatterns = [
    path('setup-church/user/<int:user_id>/', setup_church, name="setup-church"),
    path('church-settings/user/<int:user_id>/', church_settings, name="church-settings"),
]