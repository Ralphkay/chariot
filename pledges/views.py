from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from membership.models import Member
from pledges.forms import MemberMonetaryPledgeForm, MonetaryPledgeForm
from pledges.models import MemberMonetaryPledge, MonetaryPledge


def member_money_pledges(request, member_pk):
    member = Member.objects.filter(id=member_pk).get()
    member_pledges = MemberMonetaryPledge.objects.filter(pledge_person=member).order_by('updated_on')
    context = {'pledges': member_pledges, 'member': member, 'table_name': 'Member Pledge Data',
               'dbtn': 'member-pledge-download'}
    return render(request, 'pledges/member-monetary-pledges/member-money-pledges.html', context)


def create_member_money_pledge(request, member_pk):
    member = Member.objects.filter(id=member_pk).get()
    form = MemberMonetaryPledgeForm(initial={'pledge_person': member.id})
    context = {
        'form': form,
        'member': member
    }
    if request.method == 'POST':
        form = MemberMonetaryPledgeForm(request.POST, initial={'pledge_person': member.id})
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('member-money-pledges', member_pk=member.id)
        else:
            form = MemberMonetaryPledgeForm(request.POST, initial={'pledge_person': member.id})
            context = {
                'form': form,
                'member': member
            }
    return render(request, 'pledges/member-monetary-pledges/create-member-money-pledge.html', context)


def edit_member_money_pledge(request, member_pk, pledge_pk):
    member = Member.objects.filter(pk=member_pk).get()
    member_pledge = MemberMonetaryPledge.objects.filter(pledge_person=member, id=pledge_pk).get()
    form = MemberMonetaryPledgeForm(instance=member_pledge)
    context = {
        'member': member,
        'pledge': member_pledge,
        'form': form
    }
    if request.method == 'POST':
        form = MemberMonetaryPledgeForm(request.POST, instance=member_pledge)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('member-money-pledges', member_pk=member.id)
        else:
            form = MemberMonetaryPledgeForm(request.POST, instance=member_pledge)
            context = {
                'member': member,
                'pledge': member_pledge,
                'form': form
            }
    return render(request, 'pledges/member-monetary-pledges/edit-member-money-pledge.html', context)


def delete_member_money_pledge(request, member_pk, pledge_pk):
    member = Member.objects.filter(pk=member_pk).get()
    member_pledge = MemberMonetaryPledge.objects.filter(pledge_person=member, id=pledge_pk).get()
    if request.method == 'POST':
        member_pledge.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('member-money-pledges', member_pk=member.id)
    return None


def money_pledges(request):
    pledges = MonetaryPledge.objects.all().order_by('updated_on')
    context = {'pledges': pledges,'table_name': 'Monetary Pledge Data',
               'dbtn': 'monetary-pledge-download'}
    return render(request, 'pledges/monetary-pledges/money-pledges.html', context)


def create_money_pledge(request):
    form = MonetaryPledgeForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = MonetaryPledgeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('money-pledges')
        else:
            form = MonetaryPledgeForm(request.POST)
            context = {
                'form': form
            }
    return render(request, 'pledges/monetary-pledges/create-money-pledge.html', context)


def edit_money_pledge(request, pledge_pk):
    pledge = MonetaryPledge.objects.filter(id=pledge_pk).get()
    form = MonetaryPledgeForm(instance=pledge)
    context = {
        'pledge': pledge,
        'form': form
    }
    if request.method == 'POST':
        form = MonetaryPledgeForm(request.POST, instance=pledge)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('money-pledges')
        else:
            form = MonetaryPledgeForm(request.POST, instance=pledge)
            context = {
                'pledge': pledge,
                'form': form
            }
    return render(request, 'pledges/monetary-pledges/edit-money-pledge.html', context)


def delete_money_pledge(request, pledge_pk):
    pledge = MonetaryPledge.objects.filter(id=pledge_pk).get()
    if request.method == 'POST':
        pledge.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('money-pledges')
    return None