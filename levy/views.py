from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from levy.forms import LevyForm
from levy.models import Levy
from membership.models import Member
from django.urls import reverse


def levies(request, member_pk):
    member = Member.objects.filter(id=member_pk).get()
    member_levies = Levy.objects.filter(member=member)

    context = {'levies': member_levies, 'member': member,'table_name': 'Member Levy Data',
               'dbtn': 'member-levy-download'}
    return render(request, 'levy/levies.html', context)


def create_levy(request, member_pk):
    member = Member.objects.filter(id=member_pk).get()
    form = LevyForm(initial={'member': member})
    context = {
        'form': form,
        'member': member
    }
    if request.method == 'POST':
        form = LevyForm(request.POST, initial={'member': member})
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('levies', member_pk=member.id)
        else:
            form = LevyForm(request.POST, initial={'member': member})
            context = {
                'form': form,
                'member': member
            }
    return render(request, 'levy/create-levy.html', context)


def edit_levy(request, member_pk, levy_pk):
    member = Member.objects.filter(pk=member_pk).get()
    member_levy = Levy.objects.filter(member=member, id=levy_pk).get()
    form = LevyForm(instance=member_levy)
    context = {
        'member': member,
        'levy': member_levy,
        'form': form
    }
    if request.method == 'POST':
        form = LevyForm(request.POST, instance=member_levy)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('levies', member_pk=member.id)
        else:
            form = LevyForm(request.POST, initial={'member': member})

            context = {
                'member': member,
                'levy': member_levy,
                'form': form
            }
    return render(request, 'levy/edit-levy.html', context)


def delete_levy(request, member_pk, levy_pk):
    member = Member.objects.filter(pk=member_pk).get()
    member_levy = Levy.objects.filter(member=member, id=levy_pk).get()
    if request.method == 'POST':
        member_levy.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('levies', member_pk=member.id)
    return None