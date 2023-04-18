
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('single_pages.urls')),
    path('projects/', include('dashboard.urls')),
]
