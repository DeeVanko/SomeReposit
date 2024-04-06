from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # Added comma here
    path("login/", views.handlelogin, name='login'),  # Added comma here
    path("registration/", views.handleregistration, name='registration'),  # Comma added here
    
    path('translator/', views.translator_home, name='translator_home'),
    path('project-manager/', views.project_manager_home, name='project_manager_home'),
    path('chief-editor/', views.chief_editor_home, name='chief_editor_home'),
    #path("login/registration/", views.registration, name='registration'),
]
