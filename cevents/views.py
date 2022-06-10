from django.shortcuts import render, redirect

# Create your views here.
from cevents.forms import ChurchEventForm
from django.contrib import messages

from cevents.models import ChurchEvent


def events(request):
    cevents = ChurchEvent.objects.all()
    context = {
        'cevents': cevents,
        'table_name': 'Events Data',
        'dbtn': 'events-download'
    }
    print(cevents)
    return render(request, 'cevents/events.html', context)


def create_event(request):
    form = ChurchEventForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Event successfully created')
            return redirect('events')
        else:
            context = {'form': form}
    return render(request, 'cevents/create_event.html', context)


def edit_event(request, pk):
    cevent = ChurchEvent.objects.get(id=pk)
    form = ChurchEventForm(instance=cevent)
    context = {'form': form, 'event':cevent}
    if request.method == 'POST':
        form = ChurchEventForm(request.POST, instance=cevent)
        if form.is_valid():
            form.save()
            messages.success(request, f'Event successfully updated')
            return redirect('events')
        else:
            context = {'form': form, 'event': cevent}
    return render(request, 'cevents/edit_event.html', context)


def delete_event(request, pk):
    cevent = ChurchEvent.objects.get(id=pk)
    if request.method == 'POST':
        cevent.delete()
        messages.success(request, f"Event deleted successfully")
        return redirect('events')
    return None