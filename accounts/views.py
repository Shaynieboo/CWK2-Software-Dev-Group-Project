from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import TeamSelectionForm, SessionSelectionForm, HealthCheckForm, CustomUserCreationForm
from .models import Team, Session

#Author: Shayne
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


# Author: An An
# Dashboard View is used to handle sessions the user chooses.
def dashboard_view(request):
    if request.method == 'POST': # I created a form to handle the POST methods
        form = SessionSelectionForm(request.POST)
        if form.is_valid(): # checks if the form is valid 
            session = form.save(commit = False) #create instance for the session form
         #   session.user = request.user #assigns session to the user
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


# Summary View
@login_required
def summary(request):
    return render(request, 'summary.html')

# Settings View
@login_required
def settings(request):
    return render(request, 'settings.html')

