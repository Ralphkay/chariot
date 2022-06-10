from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from groups.forms import GroupForm
from groups.models import Group
from django.core.paginator import Paginator

from membership.models import Member


def groups(request):
    groups = Group.objects.all()
    context = {
        'groups': groups,
        'table_name': 'Church Groups Data',
        'dbtn': 'groups-download'
    }
    return render(request, 'groups/groups.html', context)


def number_of_members_in_organisation(org):
    number_of_members = Member.objects.filter(organisations__exact=org).count()
    return number_of_members


def edit_group(request, pk):
    organization = Group.objects.get(id=pk)
    form = GroupForm(instance=organization)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('groups')

    context = {
        'form': form,
        'organization': organization,
    }

    return render(request, 'groups/edit_group_form.html', context)


def delete_group(request, pk):
    organization = Group.objects.get(id=pk)
    if request.method == 'POST':
        organization.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('groups')
    return None


def create_group(request):
    form = GroupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('groups')
    context = {
        'form': form
    }
    return render(request, 'groups/create_group_form.html', context)