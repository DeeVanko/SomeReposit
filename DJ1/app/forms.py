from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from .models import CustomUser
import re

class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('translator', 'Translator'),
        ('project_manager', 'Project Manager'),
        ('chief_editor', 'Chief Editor'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = "Your password must contain at least 8 characters, including one capital letter, one number, and one special character."

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'user_type']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        if not re.search(r'[A-Z]', password1):
            raise ValidationError('Password must contain at least one capital letter.')
        if not re.search(r'\d', password1):
            raise ValidationError('Password must contain at least one number.')
        if not re.search(r'[!@#$%^&*()_+{}|:"<>?]', password1):
            raise ValidationError('Password must contain at least one special character.')
        return password1


User = get_user_model()
class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Invalid username or password.')
        return cleaned_data



