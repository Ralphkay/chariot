from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from churchsettings.forms import ChurchSetupForm
from churchsettings.models import ChurchSetup


def setup_church(request, user_id):
    form = ChurchSetupForm(request.POST or None, initial={'user': user_id})
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f"Church has been setup successfully")
            return redirect('dashboard-view')
        else:
            context['form'] = form

    return render(request, 'churchsettings/setup-church.html', context)


def church_settings(request, user_id):
    church = ChurchSetup.objects.filter(user=user_id).get()
    form = ChurchSetupForm(request.POST or None, instance=church)
    context ={'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('church-settings', user_id=request.user.id)
        else:
            context['form'] = form
    return render(request, 'churchsettings/church-settings.html', context)