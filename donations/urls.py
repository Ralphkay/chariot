from django.urls import path

# from membership.views import member_levy_details_view, view_member_levy, edit_member_levy, delete_member_levy
from donations.views import member_money_donations, create_member_money_donation, edit_member_money_donation, \
    delete_member_money_donation, member_item_donations, create_member_item_donation, edit_member_item_donation, \
    delete_member_item_donation, edit_money_donation, delete_money_donation, create_money_donation, money_donations

urlpatterns = [

    # general monetary donations
    path('money-donations/', money_donations, name='money-donations'),
    path('add/money-donations', create_money_donation, name='create-money-donation'),
    path('edit/money-donations/<int:donation_pk>', edit_money_donation, name='edit-money-donation'),
    path('delete/money-donations/<int:donation_pk>', delete_money_donation, name='delete-money-donation'),

    # member monetary donation urls
    path('member-money-donations/<int:member_pk>', member_money_donations, name='member-money-donations'),
    path('add/member-money-donations/<int:member_pk>', create_member_money_donation,
         name='create-member-money-donation'),
    path('edit/<int:member_pk>/member-money-donations/<int:donation_pk>', edit_member_money_donation,
         name='edit-member-money-donation'),
    path('delete/<int:member_pk>/member-money-donations/<int:donation_pk>', delete_member_money_donation,
         name='delete-member-money-donation'),

    # member item donation urls
    path('<int:member_pk>/member-item-donations', member_item_donations, name='item-donations'),
    path('add/<int:member_pk>/member-item-donations', create_member_item_donation,
         name='create-member-item-donation'),
    path('edit/<int:member_pk>/member-item-donations/<int:donation_pk>', edit_member_item_donation,
         name='edit-member-item-donation'),
    path('delete/<int:member_pk>/member-item-donations/<int:donation_pk>', delete_member_item_donation,
         name='delete-member-item-donation'),

]