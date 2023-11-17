from django.urls import path
from django.contrib.auth import views as auth_views

from account import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('images', views.images, name='images'),
    path('people', views.people, name='people')
]
