"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Login page
    path('login/', views.my_view, name='my_view'),
    # Logout page
    path('logout/', views.logout_view, name='logout_view'),
    # Registration page.
    path('register/', views.register, name='register'),
]