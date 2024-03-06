from django.db import models
from rest_framework.authtoken.admin import User


class Submission(models.Model):
    objects = None
    activity = models.ForeignKey('activity.Activity', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
