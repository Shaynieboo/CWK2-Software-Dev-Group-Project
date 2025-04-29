from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings



class Session(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.CharField(max_length=100)

    def __str__(self):
        return self.session

class Team(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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

class Setting(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #link setting model tocotumuser
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)  # Consider Django's password hashing instead

    def __str__(self):
        return f"Settings for {self.user.username}"

