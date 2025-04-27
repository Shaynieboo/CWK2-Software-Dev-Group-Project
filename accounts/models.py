from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class Session(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    session = models.CharField(max_length=100)

    def __str__(self):
        return self.session

class Team(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    team = models.CharField(max_length=50)

    def __str__(self):
        return self.team

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('engineer', 'Engineer'),
        ('team_leader', 'Team Leader'),
        ('dept_leader', 'Department Leader'),
        ('senior_manager', 'Senior Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='engineer')
# creating a custom user with a role field


