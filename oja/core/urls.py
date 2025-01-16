
m django.urls import path
from django.shortcuts import redirect
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views

"""
URL configuration for the core app.

This module defines the URL patterns and routing for core functionality like
authentication and basic navigation. It includes routes for signup, login,
logout and index redirection.

Attributes:
    app_name (str): The namespace for the app's URLs
    urlpatterns (list): List of URL patterns for routing
"""

app_name = 'core'

def redirect_to_items(request):
    """
    View function to redirect users to the items listing page.

    Args:
        request: The HTTP request object

    Returns:
        HttpResponseRedirect: Redirects to the 'item:items' URL
    """
    return redirect('item:items')

urlpatterns = [
        path('', redirect_to_items, name='index'),

        path('signup/', views.signup, name='signup'),

        path('login/',
            auth_views.LoginView.as_view(
                template_name='core/login.html',
                authentication_form=LoginForm
                ),
        path('logout/',
            auth_views.LogoutView.as_view(
                next_page='item:items'
                ),
            name='logout'),
]
