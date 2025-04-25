from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def dashboard_view(request):
    return render(request, 'pages/dashboard.html')

def team_view(request):
    return render(request, 'pages/team.html')

def instructions(request):
    return render(request, 'pages/instructions.html')

def summary(request):
    return render(request, 'summary.html')

def settings(request):
    return render(request, 'settings.html')


def card(request):
    return render(request, 'cards/card1.html')
