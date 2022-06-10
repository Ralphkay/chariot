from django.urls import path, include
from .views import add_member, add_religious_info, edit_member, delete_member, members, member

urlpatterns = [
    path('members/', members, name="members"),
    path('members/<int:pk>', member, name="member"),
    path('add-member/', add_member, name="add-member"),
    path('edit-member/<int:pk>', edit_member, name="edit-member"),
    path('delete-member/<int:pk>', delete_member, name="delete-member"),

    path('members/<int:pk>/add-religious-info/', add_religious_info, name="add-religious-info"),
    path('levies/', include('levy.urls')),
    path('welfare/', include('welfare.urls')),
    path('donations/', include('donations.urls')),
    path('pledges/', include('pledges.urls')),

]