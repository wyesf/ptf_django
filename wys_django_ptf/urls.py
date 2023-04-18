
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # allauth path

    path('blog/', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    
    path('', include('single_pages.urls')),
    path('projects/', include('single_pages.urls')),

    path('dashboard/', include('dashboard.urls')), 
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)