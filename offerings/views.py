from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.


# general monetary offering
from offerings.forms import OfferingForm, OfferingTypeForm
from offerings.models import Offering, OfferingType


def offerings(request):
    offerings = Offering.objects.all().order_by('-created_on')
    context = {'offerings': offerings, 'table_name': 'Offerings Data',
               'dbtn': 'offerings-download'}
    return render(request, 'offerings/offerings.html', context)


def create_offering(request):
    form = OfferingForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = OfferingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('offerings')
        else:
            form = OfferingForm(request.POST)
            context = {
                'form': form
            }
    return render(request, 'offerings/create-offering.html', context)


def edit_offering(request, offering_pk):
    offering = Offering.objects.filter(id=offering_pk).get()
    form = OfferingForm(instance=offering)
    context = {
        'offering': offering,
        'form': form
    }
    if request.method == 'POST':
        form = OfferingForm(request.POST, instance=offering)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('offerings')
        else:
            form = OfferingForm(request.POST, instance=offering)
            context = {
                'offering': offering,
                'form': form
            }
    return render(request, 'offerings/edit-offering.html', context)


def delete_offering(request, offering_pk):
    offering = Offering.objects.filter(id=offering_pk).get()
    if request.method == 'POST':
        offering.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('offerings')
    return None


# Offering Types
def offering_types(request):
    offering_types = OfferingType.objects.all()
    print(offering_types)
    context = {'offering_types': offering_types,'table_name': 'Offering Type Data',
               'dbtn': 'offering-type-download'}
    return render(request, 'offerings/offering-types/offering-types.html', context)


def create_offering_type(request):
    form = OfferingTypeForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = OfferingTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('offering-types')
        else:
            form = OfferingTypeForm(request.POST)
            context = {
                'form': form
            }
    return render(request, 'offerings/offering-types/create-offering-type.html', context)


def edit_offering_type(request, offering_type_pk):
    offering_type = OfferingType.objects.filter(id=offering_type_pk).get()
    form = OfferingTypeForm(instance=offering_type)
    context = {
        'offering_type': offering_type,
        'form': form
    }
    if request.method == 'POST':
        form = OfferingForm(request.POST, instance=offering_type)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('offering-types')
        else:
            form = OfferingForm(request.POST, instance=offering_type)
            context = {
                'offering_type': offering_type,
                'form': form
            }
    return render(request, 'offerings/offering-types/edit-offering-type.html', context)


def delete_offering_type(request, offering_type_pk):
    offering_type = OfferingType.objects.filter(id=offering_type_pk).get()
    if request.method == 'POST':
        offering_type.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('offering-types')
    return None