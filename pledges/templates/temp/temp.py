#
# def add_new_mmon_pledge(request):
#     pledge_form = MemberMonetaryPledgeForm()
#     context = {'form': pledge_form}
#
#     if request.method == 'POST':
#         pledge_form = MemberMonetaryPledgeForm(request.POST)
#         if pledge_form.is_valid():
#             pledge_form.save()
#             messages.success(request, f'Record added successfully')
#             return redirect('dashboard-view')
#         else:
#             print(pledge_form.errors)
#             messages.error(request, f"Record saving unsuccessful")
#             return redirect('dashboard-view')
#     return render(request, 'pledges/templates/temp/add_new_mmon_pledge.html', context)
#
#
# def add_new_mmat_pledge(request):
#     pledge_form = MemberItemPledgeForm()
#
#     context = {'form': pledge_form}
#
#     if request.method == 'POST':
#         pledge_form = MemberItemPledgeForm(request.POST)
#         if pledge_form.is_valid():
#             pledge_form.save()
#             messages.success(request, f'Record added successfully')
#             return redirect('dashboard-view')
#         else:
#             messages.error(request, f"Record saving unsuccessful")
#             return redirect('dashboard-view')
#     return render(request, 'pledges/templates/temp/add_new_mmat_pledge.html', context)
#
#
# def add_new_mon_pledge(request):
#     pledge_form = MonetaryPledgeForm()
#     context = {'form': pledge_form}
#
#     if request.method == 'POST':
#         pledge_form = MonetaryPledgeForm(request.POST)
#         if pledge_form.is_valid():
#             pledge_form.save()
#             messages.success(request, f'Record added successfully')
#             return redirect('dashboard-view')
#         else:
#             print(pledge_form.errors)
#             messages.error(request, f"Record saving unsuccessful")
#             return redirect('dashboard-view')
#
#     return render(request, 'pledges/templates/temp/add_new_mon_pledge.html', context)
#
#
# def add_new_mat_pledge(request):
#     pledge_form = ItemPledgeForm()
#     context = {'form': pledge_form}
#
#     if request.method == 'POST':
#         pledge_form = MonetaryPledgeForm(request.POST)
#         if pledge_form.is_valid():
#             pledge_form.save()
#             messages.success(request, f'Record added successfully')
#             return redirect('dashboard-view')
#         else:
#             print(pledge_form.errors)
#             messages.error(request, f"Record saving unsuccessful")
#             return redirect('dashboard-view')
#
#     return render(request, 'pledges/templates/temp/add_new_mat_pledge.html', context)
#
#
# def view_all_members_monetary_pledges_list(request):
#     all_pledges = MemberMonetaryPledge.objects.all()
#     context = {
#         'all_pledges': all_pledges
#     }
#     return render(request, 'pledges/templates/temp/view_all_members_monetary_pledges_list.html', context)
#
#
# def delete_member_pledge(request, pk):
#     pledge = MemberMonetaryPledge.objects.filter(id=pk)
#     print(pledge)
#     if pledge:
#         pledge.delete()
#         messages.success(request, f"Record deleted successfully")
#         return redirect('view_all_members_monetary_pledges_list')
#     return None
#
#
# def view_all_members_material_pledges_list(request):
#     all_pledges = MemberItemPledge.objects.all()
#     context = {
#         'all_pledges': all_pledges
#     }
#     return render(request, 'pledges/templates/temp/view_all_members_material_pledges_list.html', context)
#
#
# def view_a_member_material_pledges_list(request, pk):
#     found_member = Member.objects.filter(id=pk)
#     all_pledges = MemberItemPledge.objects.all()
#     context = {
#         'all_pledges': all_pledges,
#         'member': found_member,
#     }
#     return render(request, 'pledges/templates/temp/view_a_member_material_pledges_list.html', context)
#
#
# def view_a_member_monetary_pledges_list(request, pk):
#     found_member = Member.objects.filter(id=pk)
#     all_pledges = MemberMonetaryPledge.objects.all()
#     context = {
#         'all_pledges': all_pledges,
#         'member': found_member,
#     }
#     return render(request, 'pledges/templates/temp/view_a_member_monetary_pledges_list.html', context)
#
#
# def view_monetary_pledges_list(request):
#     all_pledges = MonetaryPledge.objects.all()
#     context = {
#         'all_pledges': all_pledges
#     }
#     return render(request, 'pledges/templates/temp/view_monetary_pledges_list.html', context)
#
#
# def view_material_pledges_list(request):
#     all_pledges = ItemPledge.objects.all()
#     context = {
#         'all_pledges': all_pledges
#     }
#     return render(request, 'pledges/templates/temp/view_material_pledges_list.html', context)