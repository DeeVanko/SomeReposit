from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Here you might perform additional validation
        
        # Check if the user exists (not necessary for registration)
        if not User.objects.filter(username=username).exists():
            # Handle non-existent user scenario
            return redirect('login')  # Redirect back to login page or show an error
        
        # Instead of directly creating a user instance, you should authenticate the user
        # However, this is just a simplified example
        user = User(username=username)
        
        # Redirect the user to another page
        return redirect('some-other-page')
    
    return render(request, 'login.html')
    
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

def handlelogin (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Here you might perform additional validation
        
        # Check if the user exists (not necessary for registration)
        if not User.objects.filter(username=username).exists():
            # Handle non-existent user scenario
            return redirect('login')  # Redirect back to login page or show an error
        
        # Instead of directly creating a user instance, you should authenticate the user
        # However, this is just a simplified example
        user = User(username=username)
        
        # Redirect the user to another page
        return redirect('NAVBAR.html')
    
    return render(request, 'login.html')
    
def handleregistration (request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    #return render(request, 'registration/register.html', {'form': form})
    return render(request, 'registration.html', {'form': form})