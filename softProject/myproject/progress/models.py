from django.db import models
from django.contrib.auth.models import User


class Progress(models.Model):
    objects = None
    activity = models.ForeignKey('activity.Activity', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    percentage = models.IntegerField(default=0)
