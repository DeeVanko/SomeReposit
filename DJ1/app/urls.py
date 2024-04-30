from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),  # Added comma here
    path("login/", views.handlelogin, name='login'),  # Added comma here
    path("registration/", views.handleregistration, name='registration'),  # Comma added here
    
    path("translator/", views.translator_home, name='translator_home'),
    path("project-manager/", views.project_manager, name='project_manager_home'),
    path("chief-editor/", views.chief_editor_home, name='chief_editor_home'),
    path("success/", views.successful_register, name='successful_register'),
    path('project/update/<int:project_id>/', views.update_project, name='update_project'),
    path("project-manager-check/", views.create_activity, name='project_manager_check'),
]
