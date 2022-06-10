from django.urls import path

import announcement
from announcement.views import create_announcement, edit_announcement, delete_announcement, announcements_view

urlpatterns=[
    path('', announcements_view, name="announcements_view"),
    path('create-announcement/', create_announcement, name="create-announcement"),
    path('<int:pk>/edit', edit_announcement, name="edit-announcement"),
    path('<int:pk>/delete', delete_announcement, name="delete-announcement"),
]