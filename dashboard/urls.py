from django.urls import path
from dashboard import views

urlpatterns = [
    # dashboard/
    path('', views.dashboard, name='dashboard'),
]