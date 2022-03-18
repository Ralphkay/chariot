from django.urls import path, include
from .views import organizations_dashboard,edit_organization,delete_organization,add_new_organization

urlpatterns = [
    path('', organizations_dashboard, name="organizations-dashboard"),
    path('add-new-organization/', add_new_organization, name="add-new-organization"),
    path('edit-organization/<int:pk>', edit_organization, name="edit-organization"),
    path('delete-organization/<int:pk>', delete_organization, name="delete-organization"),
]
