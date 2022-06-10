from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from announcement.forms import AnouncementForm
from announcement.models import Announcement


def announcements_view(request):
    announcements = Announcement.objects.all()
    context = {
        'announcements': announcements,
        'table_name': 'Announcement Data',
        'dbtn': 'announcement-download'
    }
    return render(request, 'announcement/announcement.html', context)


def create_announcement(request):
    form = AnouncementForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully created')
            return redirect('announcements_view')
        else:
            context = {'form': form}
    return render(request, 'announcement/create_announcement.html', context)


def edit_announcement(request, pk):
    announcement = Announcement.objects.get(id=pk)
    form = AnouncementForm(instance=announcement)
    context = {'form': form, 'announcement': announcement}
    if request.method == 'POST':
        form = AnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully updated')
            return redirect('announcements_view')
        else:
            context = {'form': form, 'announcement': announcement}
    return render(request, 'announcement/edit_announcement.html', context)


def delete_announcement(request, pk):
    announcement = Announcement.objects.get(id=pk)
    if request.method == 'POST':
        announcement.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('announcements_view')
    return None