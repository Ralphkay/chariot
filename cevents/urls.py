from django.urls import path
from cevents.views import create_event, events,edit_event,delete_event

urlpatterns = [
    path('', events, name='events'),
    path('create-event/', create_event, name='create-event'),
    path('<int:pk>/edit', edit_event, name='edit-event'),
    path('delete-event/<int:pk>', delete_event, name='delete-event'),
]