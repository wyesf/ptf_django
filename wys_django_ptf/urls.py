
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # allauth path
    
    path('', include('single_pages.urls')),
    path('projects/', include('single_pages.urls')),

    path('dashboard/', include('dashboard.urls')), 
]
