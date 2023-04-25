from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 
    path('', views.landing, name='index'),
    path('about_me/', views.about_me, name='about_me'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('toyproject/', views.toypjt, name='toypjt'),
    path('chart_project/', views.chartprj, name='chartprj'),
]
