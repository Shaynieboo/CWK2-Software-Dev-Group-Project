from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


# Author: An An
class Session(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.CharField(max_length=100)
    

    def __str__(self):
        return self.session

# Author: An An
class Team(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.CharField(max_length=50)

    def __str__(self):
        return self.team

# Author: An An
class Card(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    session = models.ForeignKey(Session, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    card_number = models.IntegerField()
    colour = models.CharField(max_length=20)
    progress = models.CharField(max_length=20)

    def __str__(self):
        return f"Card {self.card_number}"

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('engineer', 'Engineer'),
        ('team_leader', 'Team Leader'),
        ('dept_leader', 'Department Leader'),
        ('senior_manager', 'Senior Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='engineer')
# creating a custom user with a role field


# Author Mechelle
class Setting(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
   

    def __str__(self):
        return f"Settings for {self.user.username}"

