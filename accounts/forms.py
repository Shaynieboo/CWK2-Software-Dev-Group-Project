from django import forms
from .models import Team, Session


class TeamSelectionForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team']


class SessionSelectionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session']

