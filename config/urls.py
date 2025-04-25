from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # built-in login/logout views
    path('accounts/', include('accounts.urls')),  # custom account views like signup, dashboard, etc.
]
