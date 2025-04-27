from django import forms
from .models import Team, Session, Card

# Author: An An
class TeamSelectionForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team']

# Author: An An
class SessionSelectionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session']

# Author: An An
class HealthCheckForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['colour', 'progress']