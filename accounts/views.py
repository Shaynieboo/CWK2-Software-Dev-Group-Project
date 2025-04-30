from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import TeamSelectionForm, SessionSelectionForm, HealthCheckForm, CustomUserCreationForm
from .models import Team, Session
from django.http import HttpResponse
from .models import Setting , Card , CustomUser
from .forms import UserSettingForm

#Author: Shayne
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


# Author: An An
# Dashboard View is used to handle sessions the user chooses.

def dashboard_view(request):
    if request.method == 'POST': # I created a form to handle the POST methods
        form = SessionSelectionForm(request.POST)
        if form.is_valid(): # checks if the form is valid 
            session = form.save(commit = False) #create instance for the session form
            session.user = request.user #assigns session to the user
            session.save() # save the session to databse and redirect user to teams pae
            return redirect('team')
    else:
        form = SessionSelectionForm()
    return render(request, 'pages/dashboard.html', {'form': form})


# Author: An An
# Team View
# @login_required
def team_view(request):
    if request.method == 'POST':
        form = TeamSelectionForm(request.POST)
        if form.is_valid():
            team = form.save(commit = False) #Create instance for team form
           # team.user = request.user
            team.save() # saves team to database and directs user to instructions page
            return redirect('instructions')
        else:
            messages.error(request, "You must choose a team") # output error message if form is not valid
    else:
        form = TeamSelectionForm()
    return render(request, 'pages/team.html', {'form': form})


# Author: An An
# Instructions View
# @login_required
def instructions(request):
    return render(request, 'pages/instructions.html')

# Author: An An
# @login_required
def card(request, number):
    if request.method == 'POST': 
        form = HealthCheckForm(request.POST)
        if form.is_valid(): # checks if form is valid
            card = form.save(commit=False)
           # card.user = request.user
           # card.session = request.user.session
           # card.team  = request.user.team
            card.card_number = number
            card.save() #saves user choice to database

            next_card = number + 1

            if next_card < 12:
                return redirect(f'card/{next_card}')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, "You must choose a colour and progress") #output error message if form is invalid
    
    else:
        form = HealthCheckForm()

    return render(request, f'cards/card{number}.html', {'number' : number, 'next_card': number + 1})




# Home View (for when users first visit the base URL '/')
def home_view(request):
    return HttpResponse('<h1>Welcome to the SKY Health Check Platform!</h1><p><a href="/accounts/login/">Login Here</a></p>')

# Author Mechelle Settings View
#@login_required
def setting_view(request):
    setting, created = Setting.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserSettingForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your settings have been updated successfully!')
            return redirect('settings')
        else:
            messages.error(request, 'Correct the errors below.')
    else:
        form = UserSettingForm(instance=setting)

    return render(request, 'pages/settings.html', {'form': form})

#Engineer summary Mechelle View
#@login_required
def summary_view(request):
    user = request.user
    if user.role == 'engineer':
        sessions = Session.objects.filter(user=user)
        teams = Team.objects.filter(user=user)
        cards = Card.objects.select_related('session', 'team').filter(user=user)


        #acess to all objects from sessions teams and cards 
    elif user.role in ['team_leader', 'dept_leader', 'senior_manager']:
        sessions = Session.objects.all()
        teams = Team.objects.all()
        cards = Card.objects.select_related('session', 'team').filter(user=user) 

    
    else:
        sessions = teams = cards = []

    context = {
        'sessions': sessions,
        'teams': teams,
        'cards': cards,
    }
    return render(request, 'pages/summary.html', context)