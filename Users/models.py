# Importing Libraries
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Teams(models.Model):
    teamname = models.CharField(max_length=30)

    def __str__(self):
        return self.teamname


class Users(models.Model):
    username = models.CharField(max_length=30)
    userteam = models.ForeignKey(Teams, related_name="teams", on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class UserHappiness(models.Model):
    username = models.ForeignKey(Users, related_name="users", on_delete=models.CASCADE)
    happiness_level = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    happiness_date = models.DateField()

    def __str__(self):
        return self.username
