from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import TeamSelectionForm, SessionSelectionForm, CustomUserCreationForm
from .models import Team, Session
from django.http import HttpResponse
from .models import Setting
from .forms import UserSettingForm

# Sign up view
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            messages.success(request, "Account created successfully!")
            return redirect('role_based_redirect')  # Smart role-based redirect
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Role-based redirect view (for now just send everyone to dashboard)
@login_required
def role_based_redirect(request):
    return redirect('dashboard')

# Dashboard View
@login_required
def dashboard_view(request):
    if request.method == 'POST':
        form = SessionSelectionForm(request.POST)
        if form.is_valid():
            selected_session = form.save(commit=False)
            selected_session.user = request.user
            selected_session.save()
            return redirect('team')
    else:
        form = SessionSelectionForm()
    return render(request, 'pages/dashboard.html', {'form': form})

# Team View
@login_required
def team_view(request):
    if request.method == 'POST':
        form = TeamSelectionForm(request.POST)
        if form.is_valid():
            selected_team = form.save(commit=False)
            selected_team.user = request.user
            selected_team.save()
            request.session['selected_team'] = selected_team
            return redirect('instructions')
        else:
            messages.error(request, "You must choose a team")
    else:
        form = TeamSelectionForm()
    return render(request, 'pages/team.html', {'form': form})

# Instructions View
@login_required
def instructions(request):
    selected_team = request.session.get('selected_team')
    return render(request, 'pages/instructions.html')

# Summary View
@login_required
def summary(request):
    return render(request, 'summary.html')



# Card View
@login_required
def card(request, number):
    return render(request, f'cards/card{number}.html')

# Home View (for when users first visit the base URL '/')
def home_view(request):
    return HttpResponse('<h1>Welcome to the SKY Health Check Platform!</h1><p><a href="/accounts/login/">Login Here</a></p>')

# Settings View
@login_required
def setting_view(request):
    setting, created = Setting.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserSettingForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your settings have been updated successfully!')
            return redirect('settings')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserSettingForm(instance=setting)

    return render(request, 'settings.html', {'form': form})