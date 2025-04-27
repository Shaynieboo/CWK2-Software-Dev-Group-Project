from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import TeamSelectionForm, SessionSelectionForm, CustomUserCreationForm
from .models import Team, Session

# Sign up view
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            messages.success(request, "Account created successfully!")
            return redirect('role_based_redirect')  # go to smart redirect
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Role-based redirect view
@login_required
def role_based_redirect(request):
    return redirect('dashboard')
    # user = request.user
    # if user.role == 'engineer':
    #     return redirect('dashboard')  # you already have this view
    # elif user.role == 'team_leader':
    #     return redirect('team')  # TEMPORARY: send to team page for now
    # elif user.role == 'dept_leader':
    #     return redirect('summary')  # TEMPORARY: send to summary page for now
    # elif user.role == 'senior_manager':
    #     return redirect('summary')  # TEMPORARY: send to summary page
    # else:
    #     return redirect('login')  # fallback if role missing

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

# Settings View
@login_required
def settings(request):
    return render(request, 'settings.html')

# Card View
@login_required
def card(request, number):
    return render(request, f'cards/card{number}.html')
