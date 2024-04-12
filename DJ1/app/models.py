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
    selected_translator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    deadline = models.DateField()

    def __str__(self):
        return self.project_name
