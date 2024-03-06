from django.urls import path
from . import views

urlpatterns = [
    path('<int:submission_id>/', views.submission_detail, name='submission_detail'),
    # Add more URL patterns as needed...
]
