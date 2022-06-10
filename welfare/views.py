from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Sum
# Create your views here.
from membership.models import Member
from welfare.forms import WelfareMembershipLevyForm, WelfareForm, WelfareContributionForm
from welfare.models import WelfareMembershipLevy, Welfare, WelfareContribution
from django.core.paginator import Paginator


# welfare views/functions
def welfares(request, member_pk):
    member = Member.objects.filter(id=member_pk).get()
    member_welfare = WelfareMembershipLevy.objects.filter(member=member)
    context = {'welfares': member_welfare, 'member': member}
    return render(request, 'welfare/welfares.html', context)


def create_welfare(request, member_pk):
    member = Member.objects.filter(id=member_pk).get()
    form = WelfareMembershipLevyForm(initial={'member': member.id})
    context = {
        'form': form,
        'member': member
    }
    if request.method == 'POST':
        form = WelfareMembershipLevyForm(request.POST, initial={'member': member.id})
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('welfares', member_pk=member.id)
        else:
            form = WelfareMembershipLevyForm(request.POST, initial={'member': member.id})
            context = {
                'form': form,
                'member': member
            }
    return render(request, 'welfare/create-welfare.html', context)


def edit_welfare(request, member_pk, welfare_pk):
    member = Member.objects.filter(pk=member_pk).get()
    member_welfare = WelfareMembershipLevy.objects.filter(member=member, id=welfare_pk).get()
    form = WelfareMembershipLevyForm(instance=member_welfare)
    context = {
        'member': member,
        'welfare': member_welfare,
        'form': form
    }
    if request.method == 'POST':
        form = WelfareMembershipLevyForm(request.POST, instance=member_welfare)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('welfares', member_pk=member.id)
        else:
            form = WelfareMembershipLevyForm(request.POST, instance=member_welfare)

            context = {
                'member': member,
                'levy': member_welfare,
                'form': form
            }
    return render(request, 'welfare/edit-welfare.html', context)


def delete_welfare(request, member_pk, welfare_pk):
    member = Member.objects.filter(pk=member_pk).get()
    member_Welfare = WelfareMembershipLevy.objects.filter(member=member, id=welfare_pk).get()
    if request.method == 'POST':
        member_Welfare.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('welfares', member_pk=member.id)
    return None