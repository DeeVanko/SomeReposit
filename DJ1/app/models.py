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
