from django.db import models

# Create your models here.

class UInfo(models.Model):
    uname = models.CharField(max_length=10, default="def_uname", unique=True)
    bio = models.TextField(null=True, blank=True)
    #points = 
    #num_completed = 
    #habits = []
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

class Leaderboard(models.Model):
    pass