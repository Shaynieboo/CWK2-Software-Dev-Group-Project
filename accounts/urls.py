from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth import views as auth_views

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
urlpatterns = [
    # Custom views
    #Author Shayne
    #Author AnAn
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('team/', views.team_view, name='team'),
    path('instructions/', views.instructions, name='instructions'),
# <<<<<<< HEAD
    path('summary/', views.summary, name='summary'),
    path('settings/', views.settings_view, name='settings'), 
    path('summary/', views.summary_view, name='summary'),
    path('settings/', views.setting_view, name='settings'),
# >>>>>>> 
    path('card/<int:number>/', views.card, name='card'),
    path('redirect/', views.role_based_redirect, name='role_based_redirect'),

    #Author Shayne
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Password reset flow
    #Author Shayne
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
