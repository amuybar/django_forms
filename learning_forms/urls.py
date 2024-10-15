from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from myforms.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]
# Append static files only during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)