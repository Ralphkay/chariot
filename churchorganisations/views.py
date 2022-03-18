from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from churchorganisations.forms import ChurchOrganisationForm
from churchorganisations.models import ChurchOrganisation
from django.core.paginator import Paginator

from membership.models import Member


def organizations_dashboard(request):
    organizations = ChurchOrganisation.objects.all()
    paginator = Paginator(organizations, 10)
    # Show 5 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'organizations': organizations,
        'page_obj': page_obj
    }
    return render(request, 'churchorganisations/church-organizations.html', context)


def number_of_members_in_organisation(org):
    number_of_members = Member.objects.filter(organisations__exact=org).count()
    return number_of_members


def edit_organization(request, pk):
    organization = ChurchOrganisation.objects.get(id=pk)
    form = ChurchOrganisationForm(instance=organization)
    if request.method == 'POST':
        form = ChurchOrganisationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('organizations-dashboard')

    context = {
        'form': form,
        'organization': organization,
    }

    return render(request, 'churchorganisations/edit_organisation.html', context)


def delete_organization(request, pk):
    organization = ChurchOrganisation.objects.get(id=pk)
    if request.method == 'POST':
        if organization:
            organization.delete()
            messages.success(request, f"Record deleted successfully")
            return redirect('organizations-dashboard')
    return None


def add_new_organization(request):
    form = ChurchOrganisationForm()
    if request.method == 'POST':
        form = ChurchOrganisationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('organizations-dashboard')
    context = {
        'form': form
    }

    return render(request, 'churchorganisations/add_new_organization.html', context)
