from django.urls import path, include

from pledges.views import add_new_mmat_pledge, add_new_mmon_pledge, view_all_members_monetary_pledges_list, \
    view_all_members_material_pledges_list, view_a_member_material_pledges_list, view_a_member_monetary_pledges_list, \
    add_new_mon_pledge, add_new_mat_pledge, delete_member_pledge

urlpatterns = [
    path('add-new-member-monetary-pledge', add_new_mmon_pledge, name='add_new_mmon_pledge'),
    path('add-new-member-material-pledge', add_new_mmat_pledge, name='add_new_mmat_pledge'),
    path('add-new-material-pledge', add_new_mon_pledge, name='add_new_mon_pledge'),
    path('add-new-material-pledge', add_new_mat_pledge, name='add_new_mat_pledge'),
    path('all-members-material-pledge', view_all_members_material_pledges_list, name='view_all_members_material_pledges_list'),
    path('all-members-monetary-pledge', view_all_members_monetary_pledges_list, name='view_all_members_monetary_pledges_list'),
    path('<int:pk>/delete-member-monetary-pledge', delete_member_pledge, name='delete_member_pledge'),
    path('<int:member_id>/a-member-material-pledge-list/', view_a_member_material_pledges_list, name='view_a_member_material_pledges_list'),
    path('<int:member_id>/a-member-monetary-pledge-list', view_a_member_monetary_pledges_list, name='view_a_member_monetary_pledges_list'),
]