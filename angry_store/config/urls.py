from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.shortcuts import render

# Custom error handlers
def permission_denied_view(request, exception=None):
    return render(request, '403.html', status=403)

handler403 = permission_denied_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
