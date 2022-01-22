from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from membership.models import Member
from welfare.models import WelfareMembershipLevy


def view_welfare_levy_payment_list(request, pk):
    found_member = get_object_or_404(Member, pk=pk)
    welfare_payments_by_member = WelfareMembershipLevy.objects.filter(member=found_member).order_by('-created_on')
    context = {
        'member': found_member,
        'welfare_payments_by_member': welfare_payments_by_member,
        'page_title': f"{found_member}-Welfare Levy Payments"
    }
    return render(request, 'welfare/welfare_payment_list.html', context)


def pay_welfare_levy(request, pk):
    found_member = get_object_or_404(Member, pk=pk)
    pay_welfare_levy_form =
    pass


def delete_welfare_levy_payment(request, pk, payment):
    found_member = get_object_or_404(Member, pk=pk)
    welfare_payments_by_member = WelfareMembershipLevy.objects.filter(member=found_member, id=pk).first()
    if welfare_payments_by_member:
        welfare_payments_by_member.delete()
        return redirect(request,'view_welfare_levy_payment_list')
    return None