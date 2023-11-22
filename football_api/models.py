from django.db import models


class CreateNewMatch(models.Model):
    """This model for create game schedule"""
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"


class SendMessageToEmail(models.Model):
    """This model for send game link to user"""
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = 'blogpost'

    def __str__(self):
        return self.email
