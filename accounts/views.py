from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TeamSelectionForm, SessionSelectionForm
from django.contrib import messages
from .models import Team, Session

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def dashboard_view(request):
    if request.method == 'POST':
        form = SessionSelectionForm(request.POST)
        if form.is_valid():
            print("form valid")
            selected_session = form.save(commit = False)
            selected_session.user = request.user
            selected_session.save()
            return redirect('team')
    else:
        form = SessionSelectionForm()


    return render(request, 'pages/dashboard.html', {'form' : form})

@login_required
def team_view(request):
    if request.method == 'POST':
        form = TeamSelectionForm(request.POST)
        if form.is_valid():
            selected_team = form.save(commit = False)
            selected_team.user = request.user
            selected_team.save()
            request.session['selected_team'] = selected_team
            print("Redirecting to instructions page")

            return redirect('instructions')
        
        else:
            messages.error(request, "You must choose a team")

    else:
        form = TeamSelectionForm()     
    
    return render(request, 'pages/team.html', {'form' : form})

@login_required
def instructions(request):
    selected_team = request.session.get('selected_team')
    return render(request, 'pages/instructions.html')

def summary(request):
    return render(request, 'summary.html')

def settings(request):
    return render(request, 'settings.html')


def card(request, number):
    return render(request, f'cards/card{number}.html')