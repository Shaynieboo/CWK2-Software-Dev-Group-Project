from django import forms
from .models import Team, Session
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser , Setting

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'password1', 'password2')
#  allows new users to choose their role when signing up.

class TeamSelectionForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team']


class SessionSelectionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session']

class UserSettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ['name', 'email','username']  # only editable fields