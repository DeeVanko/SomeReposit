from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    progress = models.IntegerField(default=0)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)  # translator, chief editor, project manager
