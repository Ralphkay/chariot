from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from donations.forms import MemberMonetaryDonationForm, MemberItemDonationForm, MonetaryDonationForm
from donations.models import MemberMonetaryDonation, MemberItemDonation, MonetaryDonation
from membership.models import Member


def member_money_donations(request, member_pk):
    member = Member.objects.filter(id=member_pk).get()
    member_donations = MemberMonetaryDonation.objects.filter(member=member).order_by('-created_on')
    context = {'donations': member_donations, 'member': member}
    return render(request, 'donations/member-money-donations.html', context)


def create_member_money_donation(request, member_pk):
    member = Member.objects.filter(id=member_pk).get()
    form = MemberMonetaryDonationForm(initial={'member': member})
    context = {
        'form': form,
        'member': member
    }
    if request.method == 'POST':
        form = MemberMonetaryDonationForm(request.POST, initial={'member': member})
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('member-money-donations', member_pk=member.id)
        else:
            form = MemberMonetaryDonationForm(request.POST, initial={'member': member})
            context = {
                'form': form,
                'member': member
            }
    return render(request, 'donations/create-donation.html', context)


def edit_member_money_donation(request, member_pk, donation_pk):
    member = Member.objects.filter(pk=member_pk).get()
    member_donation = MemberMonetaryDonation.objects.filter(member=member, id=donation_pk).get()
    form = MemberMonetaryDonationForm(instance=member_donation)
    context = {
        'member': member,
        'donation': member_donation,
        'form': form
    }
    if request.method == 'POST':
        form = MemberMonetaryDonationForm(request.POST, instance=member_donation)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('member-money-donations', member_pk=member.id)
        else:
            form = MemberMonetaryDonationForm(request.POST, instance=member_donation)
            context = {
                'member': member,
                'donation': member_donation,
                'form': form
            }
    return render(request, 'donations/edit-donation.html', context)


def delete_member_money_donation(request, member_pk, donation_pk):
    member = Member.objects.filter(pk=member_pk).get()
    member_donation = MemberMonetaryDonation.objects.filter(member=member, id=donation_pk).get()
    if request.method == 'POST':
        member_donation.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('member-money-donations', member_pk=member.id)
    return None


# member items donations

def member_item_donations(request, member_pk):
    member = Member.objects.filter(id=member_pk).get()
    member_donations = MemberItemDonation.objects.filter(member=member).order_by('-created_on')
    context = {'donations': member_donations, 'member': member, 'table_name': 'Member Donation Item Data',
               'dbtn': 'member-donation-item-download'}
    return render(request, 'donations/member-item-donations.html', context)


def create_member_item_donation(request, member_pk):
    member = Member.objects.filter(id=member_pk).get()
    form = MemberItemDonationForm(initial={'member': member})
    context = {
        'form': form,
        'member': member
    }
    if request.method == 'POST':
        form = MemberItemDonationForm(request.POST, initial={'member': member})
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('item-donations', member_pk=member.id)
        else:
            form = MemberItemDonationForm(request.POST, initial={'member': member})
            context = {
                'form': form,
                'member': member
            }
    return render(request, 'donations/item-donations/create-member-item-donation.html', context)


def edit_member_item_donation(request, member_pk, donation_pk):
    member = Member.objects.filter(pk=member_pk).get()
    member_donation = MemberItemDonation.objects.filter(member=member, id=donation_pk).get()
    form = MemberItemDonationForm(instance=member_donation)
    context = {
        'member': member,
        'donation': member_donation,
        'form': form
    }
    if request.method == 'POST':
        form = MemberItemDonationForm(request.POST, instance=member_donation)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('item-donations', member_pk=member.id)
        else:
            form = MemberItemDonationForm(request.POST, instance=member_donation)
            context = {
                'member': member,
                'donation': member_donation,
                'form': form
            }
    return render(request, 'donations/item-donations/edit-member-item-donation.html', context)


def delete_member_item_donation(request, member_pk, donation_pk):
    member = Member.objects.filter(pk=member_pk).get()
    member_donation = MemberItemDonation.objects.filter(member=member, id=donation_pk).get()
    if request.method == 'POST':
        member_donation.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('item-donations', member_pk=member.id)
    return None


# general monetary donations
def money_donations(request):
    donations = MonetaryDonation.objects.all().order_by('-created_on')
    context = {'donations': donations, 'table_name': 'General Donations Data', 'dbtn': 'donation-download'}
    return render(request, 'donations/monetary-donations/money-donations.html', context)


def create_money_donation(request):
    form = MonetaryDonationForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = MonetaryDonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('money-donations')
        else:
            form = MonetaryDonationForm(request.POST)
            context = {
                'form': form
            }
    return render(request, 'donations/monetary-donations/create-money-donation.html', context)


def edit_money_donation(request, donation_pk):
    donation = MonetaryDonation.objects.filter(id=donation_pk).get()
    form = MonetaryDonationForm(instance=donation)
    context = {
        'donation': donation,
        'form': form
    }
    if request.method == 'POST':
        form = MonetaryDonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('money-donations')
        else:
            form = MonetaryDonationForm(request.POST, instance=donation)
            context = {
                'donation': donation,
                'form': form
            }
    return render(request, 'donations/monetary-donations/edit-money-donation.html', context)


def delete_money_donation(request, donation_pk):
    donation = MonetaryDonation.objects.filter(id=donation_pk).get()
    if request.method == 'POST':
        donation.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('money-donations')
    return None