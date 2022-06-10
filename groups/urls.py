from django.urls import path, include
from .views import groups, edit_group, delete_group, create_group

urlpatterns = [
    path('all/', groups, name="groups"),
    path('create-group/', create_group, name="create-group"),
    path('edit-group/<int:pk>', edit_group, name="edit-group"),
    path('delete-group/<int:pk>', delete_group, name="delete-group"),
]