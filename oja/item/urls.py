from django.urls import path
from . import views

"""
URL configuration for the conversation app.

This module defines URL patterns for conversation-related views including
inbox, conversation details, and creating new conversations.
"""

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
]
