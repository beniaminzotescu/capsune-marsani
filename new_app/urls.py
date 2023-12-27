from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from new_app import settings


urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
