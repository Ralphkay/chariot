from django.urls import path, include
from .views import expenses, edit_expense, delete_expense, create_expense

urlpatterns = [
    path('all/', expenses, name="expenses"),
    path('create-expense/', create_expense, name="create-expense"),
    path('edit-expense/<int:pk>', edit_expense, name="edit-expense"),
    path('delete-expense/<int:pk>', delete_expense, name="delete-expense"),
]