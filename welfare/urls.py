from django.urls import path

from welfare.views import delete_welfare, edit_welfare, welfares, create_welfare

urlpatterns = [
    # welfare
    # path('welfare/<int:pk>', view_welfare, name="view-welfare"),
    # path('setup-welfare', setup_welfare, name="setup-welfare"),
    # path('welfare-setup-list', welfare_setup_list, name="welfare-setup-list"),
    # path('<int:pk>/delete', delete_welfare, name="delete-welfare"),
    # path('<int:pk>/edit', edit_welfare, name="edit-welfare"),
    #
    # path('member/<int:pk>/levy-payments', view_welfare_levy_payment_list, name="view_welfare_levy_payment_list"),
    # path('member/<int:pk>/pay-welfare-levy', pay_welfare_levy, name="pay_welfare_levy"),
    # path('member/<int:pk>/levy-payments/<int:payment>/delete', delete_welfare_levy_payment,
    #      name="delete_welfare_levy_payment"),
    #
    # # General  contributions
    # path('member/<int:pk>/contributions', view_contributions_paid_list, name="view-contributions-paid-list"),
    # path('member/<int:pk>/pay-contribution-levy', pay_contribution_levy, name="pay-contribution-levy"),
    # path('member/<int:pk>/contributions-levy-payments/<int:payment>/delete', delete_contribution_levy_payment,
    #      name="delete-contribution-levy-payment"),

    # Pledges route
    # path('/member/<int:pk>/levy-payments', view_pledges_paid_list, name="view-pledges-paid-list"),

    path('<int:member_pk>/welfare', welfares, name='welfares'),
    path('add/<int:member_pk>/welfare', create_welfare, name='create-welfare'),
    path('edit/<int:member_pk>/welfare/<int:welfare_pk>', edit_welfare, name='edit-welfare'),
    path('delete/<int:member_pk>/welfare/<int:welfare_pk>', delete_welfare, name='delete-welfare'),
]