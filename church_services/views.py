from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from church_services.forms import ChurchServiceForm
from church_services.models import ChurchService


def church_services(request):
    church_services = ChurchService.objects.all()

    context = {'services': church_services, 'table_name': 'Church Services Data',
               'dbtn': 'church-service-download'}
    return render(request, 'church_services/services.html', context)


def create_service(request):
    form = ChurchServiceForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ChurchServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('church_services')
        else:
            form = ChurchServiceForm(request.POST)
            context = {
                'form': form
            }
    return render(request, 'church_services/create-service.html', context)


def edit_service(request, service_pk):
    service = ChurchService.objects.filter(id=service_pk).get()
    form = ChurchServiceForm(instance=service)
    context = {
        'service': service,
        'form': form
    }
    if request.method == 'POST':
        form = ChurchServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('church_services')
        else:
            form = ChurchServiceForm(request.POST, instance=service)
            context = {
                'service': service,
                'form': form
            }
    return render(request, 'church_services/edit-service.html', context)


def delete_service(request, service_pk):
    service = ChurchService.objects.filter(id=service_pk).get()
    if request.method == 'POST':
        service.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('church_services')
    return None