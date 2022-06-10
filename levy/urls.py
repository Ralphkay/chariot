from django.urls import path
from levy.views import levies,edit_levy, delete_levy, create_levy

urlpatterns = [

    path('<int:member_pk>/monthly-levies/', levies, name='levies'),
    path('create/<int:member_pk>/monthly-levy/', create_levy, name='create-levy'),
    path('edit/<int:member_pk>/monthly-levy/<int:levy_pk>/', edit_levy, name='edit-levy'),
    path('delete/<int:member_pk>/monthly-levy/<int:levy_pk>/', delete_levy, name='delete-levy'),
]