from django.db import models
from django.contrib.auth.models import User

# Author: An An
class Session(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    session = models.CharField(max_length=100)
    

    def __str__(self):
        return self.session

# Author: An An
class Team(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    team = models.CharField(max_length=50)

    def __str__(self):
        return self.team

# Author: An An
class Card(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    session = models.ForeignKey(Session, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    card_number = models.IntegerField()
    colour = models.CharField(max_length=20)
    progress = models.CharField(max_length=20)

    def __str__(self):
        return f"Card {self.card_number}"