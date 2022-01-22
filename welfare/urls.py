from django.urls import path

from welfare.views import view_welfare_levy_payment_list,delete_welfare_levy_payment

urlpatterns = [
    path('/levy-payments', view_welfare_levy_payment_list, name="view_welfare_levy_payment_list"),
    path('/levy-payments/<int:payment>/delete', delete_welfare_levy_payment, name="delete_welfare_levy_payment"),
]
