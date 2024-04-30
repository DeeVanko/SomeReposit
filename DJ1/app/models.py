from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('translator', 'translator'),
        ('project_manager', 'project_manager'),
        ('chief_editor', 'chief_editor'),
    ]

    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)

    # Define custom related_name for groups and user_permissions fields
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    deadline = models.DateField()
    status = models.CharField(max_length=20, default='Not completed', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

class Activity(models.Model):
    activity_name = models.CharField(max_length=255)
    translator = models.CharField(max_length=255)
    deadline = models.DateField()
    remaining_text_volume = models.CharField(max_length=100, default="0%")
    status = models.CharField(max_length=100, default="Not Completed")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="activities")

    def __str__(self):
        return self.activity_name