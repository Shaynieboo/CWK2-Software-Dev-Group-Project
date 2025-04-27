from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('team/', views.team_view, name='team'),
    path('instructions/', views.instructions, name='instructions'),
    path('summary/', views.summary, name='summary'),
    path('settings/', views.settings, name='settings'),
    path('card/<int:number>/', views.card, name='card'),
    path('redirect/', views.role_based_redirect, name='role_based_redirect'),

]
