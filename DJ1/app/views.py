from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .forms import RailwayAuthenticationForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def handlelogin(request):
    if request.method == 'POST':
        form = RailwayAuthenticationForm(request.POST)
        if form.is_valid():
            # Authentication is handled in the form's clean() method
            return redirect('about')  # Redirect to the next page upon successful login
    else:
        form = RailwayAuthenticationForm()
    return render(request, 'login.html', {'form': form})

    
def handleregistration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user object returned by form.save()
            # You might want to log the user in automatically after registration
            # This can be done using Django's authentication system
            # For example: login(request, user)
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})
