from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def index (request):
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')

def contact (request):
    return render(request, 'contact.html')

def handlelogin (request):
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

