from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from accounts.decorators import allowed_roles, check_if_setup, login_not_required
from accounts.email import send_mail
from churchclicks.settings import mailjet
from django.http import HttpResponse


# @login_not_required
from donations.models import MonetaryDonation, MemberMonetaryDonation
from expenses.models import Expense
from membership.models import Member
from offerings.models import Offering
from projects.models import Project


def dashboard(request):
    total_offerings = Offering.objects.all().aggregate(Sum('amount'))
    total_monetary_donation = MonetaryDonation.objects.all().aggregate(Sum('amount'))
    total_projects = Project.objects.all().count()
    total_members = Member.objects.all().count()
    total_member_monetary_donation = MemberMonetaryDonation.objects.all().aggregate(Sum('amount'))
    total_expenses = Expense.objects.all().aggregate(Sum('amount'))
    if total_monetary_donation['amount__sum'] is None:
        total_monetary_donation['amount__sum'] = 0
    elif total_member_monetary_donation['amount__sum'] is None:
        total_member_monetary_donation['amount__sum'] = 0
    elif total_offerings['amount__sum'] is None:
        total_offerings['amount__sum'] = 0

    total_contributions = float(total_offerings['amount__sum']) + float(total_monetary_donation['amount__sum']) + float(total_member_monetary_donation['amount__sum'])
    # + float(total_monetary_donation) + float(total_member_monetary_donation)
    print(total_contributions)
    context = {'total_expenses': round(total_expenses['amount__sum'], 2), 'total_projects': total_projects,
               'total_members': total_members, 'total_contributions': round(total_contributions, 2)}
    return render(request, 'dashboard/dashboard.html', context)


def runurl(request, token):
    return HttpResponse("Kit surfing")