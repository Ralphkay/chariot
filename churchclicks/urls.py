from django.contrib import admin
from django.urls import path, include

from churchclicks import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('membership/', include('membership.urls')),
                  path('groups/', include('groups.urls')),
                  path('dashboard/', include('dashboard.urls')),
                  path('events/', include('cevents.urls')),
                  path('announcement/', include('announcement.urls')),
                  path('offerings/', include('offerings.urls')),
                  path('church-services/', include('church_services.urls')),
                  path('projects/', include('projects.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('expenses/', include('expenses.urls')),
                  path('church/', include('churchsettings.urls')),
                  path('cashbook/', include('cashbook.urls')),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)