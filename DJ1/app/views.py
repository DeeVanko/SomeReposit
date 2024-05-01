from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .forms import CustomAuthenticationForm
from .models import CustomUser, Project, Activity
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import connection
from .forms import ProjectForm, ActivityForm
from django.http import JsonResponse



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def handlelogin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'translator':
                    return redirect('translator_home')
                elif user.user_type == 'project_manager':
                    return redirect('project_manager_home')
                elif user.user_type == 'chief_editor':
                    return redirect('chief_editor_home')
                # Add more user type conditions as needed
            else:
                # Handle invalid login
                # Redirect back to login page or display an error message
                pass
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

    
def handleregistration(request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user_type = form.cleaned_data['user_type']

            # Create a new CustomUser object and save it to the database
                new_user = CustomUser.objects.create_user(username=username, password=password, user_type=user_type)

                return redirect('successful_register')  # Redirect to the login page after successful registration
        else:
            form = UserRegistrationForm()
        return render(request, 'registration.html', {'form': form})

def translator_home(request):
    # Your logic for translator home page
    return render(request, 'translator_home.html')



def chief_editor_home(request):
    # Your logic for chief editor home page
    return render(request, 'chief_editor_home.html')

def successful_register(request):
    # Your logic for translator home page
    return render(request, 'successful_register.html')

def project_manager(request):
    projects = Project.objects.all().order_by('-created_at')  # Retrieve all projects
    user = request.user  # Get the current user
    translators = CustomUser.objects.filter(user_type='translator')
    activities = Activity.objects.all()  # Retrieve all activities

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # Save the project with the current user as the selected_translator
            project = form.save(commit=False)
            
            project.save()
            return redirect('project_manager_home')  # Redirect after successful form submission
    else:
        form = ProjectForm()

    context = {
        'projects': projects,
        'user': user,
        'form': form,
        'translators': translators,
        'activities': activities,  # Pass activities to the template context
    }
    return render(request, 'project_manager_home.html', context)


def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_manager_home')  # Replace with your actual home view
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})

def create_activity(request):
    projects = Project.objects.all()  # Fetch all projects for the dropdown
    translators = CustomUser.objects.filter(user_type='translator')  # Assuming CustomUser is your user model with a 'user_type' field

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        print(request.POST)
        if form.is_valid():
            
            activity = form.save(commit=False)
            activity.remaining_text_volume = "0%"
            activity.status = "Not Completed"
            activity.save()
            
            return redirect('project_manager_home')  # Redirect to a home or appropriate page
        else:
            print(form.is_valid())
    else:
        form = ActivityForm()

    return render(request, 'project_manager_home.html', {'form': form, 'projects': projects, 'translators': translators})
