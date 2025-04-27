from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


from .forms import CustomUserCreationForm

# Sign up view
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            messages.success(request, "Account created successfully!")
            return redirect('role_based_redirect')  # 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Role-based redirect view
@login_required
def role_based_redirect(request):
    user = request.user
    if user.role == 'engineer':
        return redirect('dashboard')  # name of our dashboard url
    elif user.role == 'team_leader':
        return redirect('team_leader_dashboard')
    elif user.role == 'dept_leader':
        return redirect('department_summary')
    elif user.role == 'senior_manager':
        return redirect('senior_manager_summary')
    else:
        return redirect('login')
        