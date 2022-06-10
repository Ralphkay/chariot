from django.urls import path, include

from pledges.views import member_money_pledges, create_money_pledge, edit_money_pledge, delete_money_pledge \
    , create_member_money_pledge, edit_member_money_pledge, delete_member_money_pledge, money_pledges

urlpatterns = [

    path('money-pledges/', money_pledges, name='money-pledges'),
    path('add/money-pledges/', create_money_pledge, name='create-money-pledge'),
    path('edit/money-pledges/<int:pledge_pk>/', edit_money_pledge, name='edit-money-pledge'),
    path('delete/money-pledges/<int:pledge_pk>/', delete_money_pledge, name='delete-money-pledge'),


    path('<int:member_pk>/member-money-pledges', member_money_pledges, name='member-money-pledges'),
    path('add/<int:member_pk>/member-money-pledges', create_member_money_pledge, name='create-member-money-pledge'),
    path('edit/<int:member_pk>/member-money-pledges/<int:pledge_pk>', edit_member_money_pledge, name='edit-member-money-pledge'),
    path('delete/<int:member_pk>/member-money-pledges/<int:pledge_pk>', delete_member_money_pledge, name='delete-member-money-pledge'),

]