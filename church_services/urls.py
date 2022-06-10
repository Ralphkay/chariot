from django.urls import path

from church_services.views import delete_service, edit_service, create_service, church_services

urlpatterns = [
    path('', church_services, name='church_services'),
    path('add/', create_service, name='create-service'),
    path('edit/<int:service_pk>', edit_service, name='edit-service'),
    path('delete/<int:service_pk>', delete_service, name='delete-service'),
]