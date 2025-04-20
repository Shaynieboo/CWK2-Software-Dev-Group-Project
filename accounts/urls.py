from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name = 'dashboard'),
    path ('team/', views.team_view, name = 'team'),
    path ('instructions/', views.instructions, name = 'instructions'),
    path('summary/', views.summary, name = 'summary'),
     path('settings/', views.settings, name = 'settings'),
]
