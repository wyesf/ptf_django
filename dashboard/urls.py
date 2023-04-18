from django.urls import path
from . import views

urlpatterns = [
    # dashboard/
    path('', views.dashboard, name='projects'),
]