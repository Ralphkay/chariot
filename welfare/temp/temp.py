#
# def view_welfare_levy_payment_list(request, pk):
#     found_member = get_object_or_404(Member, pk=pk)
#     welfare_payments_by_member = WelfareMembershipLevy.objects.filter(member=found_member).order_by('-created_on')
#     pay_welfare_levy_form = WelfareMembershipLevyForm(initial={'member': found_member})
#
#     paginator = Paginator(welfare_payments_by_member, 5)  # Show 5 contacts per page.
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         'member': found_member,
#         'welfare_payments_by_member': welfare_payments_by_member,
#         'page_title': f"{found_member}-Welfare Levy Payments",
#         'form': pay_welfare_levy_form,
#         'page_obj': page_obj
#     }
#     return render(request, 'welfare/templates/temp/welfare_payment_list.html', context)
#
#
# def view_welfare_lists(request):
#     all_welfare = Welfare.objects.all()
#     context = {
#         'all_welfare': all_welfare
#     }
#     return render(request, 'welfare/welfare_lists.html', context)
#
#
# def add_welfare(request):
#     welfare_add_form = WelfareForm()
#     if request.method == 'POSTS':
#         welfare_add_form = WelfareForm(request.POST)
#         if welfare_add_form.is_valid():
#             welfare_add_form.save()
#             messages.success(request, f"Record added successfully")
#             return redirect('view_welfare_lists')
#     context = {
#         'form': welfare_add_form
#     }
#     return render(request, 'welfare/welfare_lists.html', context)
#
#
#
#
#
# # welfare_levy functions
# def pay_welfare_levy(request, pk):
#     found_member = get_object_or_404(Member, pk=pk)
#     pay_welfare_levy_form = WelfareMembershipLevyForm()
#     if request.method == 'POST':
#         pay_welfare_levy_form = WelfareMembershipLevyForm(request.POST)
#         if pay_welfare_levy_form.is_valid():
#             pay_welfare_levy_form.save()
#             messages.success(request, f'Record deleted successfully')
#             return redirect('view_welfare_levy_payment_list', pk=found_member.id)
#         else:
#             messages.error(request, f"Record saving unsuccessful")
#             return redirect('view_welfare_levy_payment_list', pk=found_member.id)
#     context = {
#         'member': found_member,
#         'form': pay_welfare_levy_form
#     }
#     return render(request, 'welfare/templates/temp/welfare_payment_list.html', context)
#
#
# def delete_welfare_levy_payment(request, pk, payment):
#     found_member = get_object_or_404(Member, pk=pk)
#     welfare_payments_by_member = WelfareMembershipLevy.objects.filter(member=found_member, id=payment).first()
#     if welfare_payments_by_member:
#         welfare_payments_by_member.delete()
#         messages.success(request, f"Record deleted successfully")
#         return redirect('view_welfare_levy_payment_list', pk=found_member.id)
#
#
# # welfare contribution functions
# def view_contributions_paid_list(request, pk):
#     found_member = get_object_or_404(Member, pk=pk)
#     contributions_payments_by_member = WelfareContribution.objects.filter(member=found_member).order_by('-created_on')
#     pay_contribution_levy_form = WelfareContributionForm(initial={'member': found_member})
#
#     paginator = Paginator(contributions_payments_by_member, 5)
#     # Show 5 contacts per page.
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {
#         'member': found_member,
#         'welfare_payments_by_member': contributions_payments_by_member,
#         'page_title': f"{found_member}-General Contributions Payments",
#         'form': pay_contribution_levy_form,
#         'page_obj': page_obj
#     }
#     return render(request, 'welfare/templates/temp/contributions_payment_list.html', context)
#
#
# def pay_contribution_levy(request, pk):
#     found_member = get_object_or_404(Member, pk=pk)
#     pay_welfare_contribution_form = WelfareContributionForm()
#     if request.method == 'POST':
#         pay_welfare_contribution_form = WelfareContributionForm(request.POST)
#         if pay_welfare_contribution_form.is_valid():
#             pay_welfare_contribution_form.save()
#             messages.success(request, f'Record deleted successfully')
#             return redirect('view-contributions-paid-list', pk=found_member.id)
#         else:
#             messages.error(request, f"Record saving unsuccessful")
#             return redirect('view-contributions-paid-list', pk=found_member.id)
#     context = {
#         'member': found_member,
#         'form': pay_welfare_contribution_form
#     }
#     return render(request, 'welfare/templates/temp/contributions_payment_list.html', context)
#
#
# def delete_contribution_levy_payment(request, pk, payment):
#     found_member = get_object_or_404(Member, pk=pk)
#     contributions_payments_by_member = WelfareContribution.objects.filter(member=found_member, id=payment).first()
#     if contributions_payments_by_member:
#         contributions_payments_by_member.delete()
#         messages.success(request, f"Record deleted successfully")
#         return redirect('view-contributions-paid-list', pk=found_member.id)
#     return None
#
#
# def setup_welfare(request):
#     form = WelfareForm()
#     if request.method == 'POST':
#         form = WelfareForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f"Record saved successfully")
#             return redirect('welfare-setup-list')
#     context = {
#         'form': form
#     }
#     return render(request, 'welfare/templates/temp/setup-welfare.html', context)
#
#
# def welfare_setup_list(request):
#     welfares = Welfare.objects.all()
#
#     context = {
#         'welfare_list': welfares
#     }
#     return render(request, 'welfare/templates/temp/welfare_setup_list.html', context)
#  def delete_welfare(request, pk):
#     welfare = Welfare.objects.filter(id=pk)
#     if welfare:
#         welfare.delete()
#         messages.success(request, f"Record deleted successfully")
#         return redirect('all_welfare_list')
#     return None
# def view_welfare(request, pk):
#     welfare = get_object_or_404(Welfare, id=pk)
#     welfare_contributions_grouped_by_member = WelfareContribution.objects.filter(welfare=welfare). \
#         values('member__first_name', 'member__middle_name', 'member__last_name', 'member__id').annotate(
#         Sum('amount_contributed'))
#
#     total_contributions = WelfareContribution.objects.filter(welfare=welfare).aggregate(Sum('amount_contributed'))
#     print("totals", total_contributions)
#     context = {
#         'welfare': welfare,
#         'welfare_contributions_grouped_by_member': welfare_contributions_grouped_by_member,
#         'total_contributions': total_contributions,
#         'page_title': f"{welfare} contribution details"
#     }
#     return render(request, 'welfare/templates/temp/_contributions_details.html', context)