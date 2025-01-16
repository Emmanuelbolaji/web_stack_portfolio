"""
URLconf for the dashboard application.

This module defines the URL patterns for the dashboard application, 
mapping URLs to the corresponding views.
"""

from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]
