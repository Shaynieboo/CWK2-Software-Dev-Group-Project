from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TeamSelectionForm, SessionSelectionForm, HealthCheckForm
from django.contrib import messages
from .models import Team, Session, Card

#Author: Shayne
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Author: An An
@login_required
def dashboard_view(request):
    if request.method == 'POST':
        form = SessionSelectionForm(request.POST)
        if form.is_valid():
            session = form.save(commit = False)
            session.user = request.user
            session.save()
            form.save()
            return redirect('team')
    else:
        form = SessionSelectionForm()


    return render(request, 'pages/dashboard.html', {'form' : form})

# Author: An An
@login_required
def team_view(request):
    if request.method == 'POST':
        form = TeamSelectionForm(request.POST)
        if form.is_valid():
            team = form.save(commit = False)
            team.user = request.user
            team.save()
            form.save()
            return redirect('instructions')
        
        else:
            messages.error(request, "You must choose a team")

    else:
        form = TeamSelectionForm()     
    
    return render(request, 'pages/team.html', {'form' : form})

# Author: An An

def instructions(request):
    return render(request, 'pages/instructions.html')

# Author: An An

def card(request, number):
    if request.method == 'POST':
        form = HealthCheckForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.session = request.user.session
            card.team  = request.user.team
            card.card_number = number
            card.save()

            if number < 10:
                return redirect(f'card/{number + 1}')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, "You must choose a colour and progress")
    
    else:
        form = HealthCheckForm()

    return render(request, f'cards/card{number}.html')


@login_required
def summary(request):
    return render(request, 'summary.html')

@login_required
def settings(request):
    return render(request, 'settings.html')


