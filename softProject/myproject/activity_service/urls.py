from django.urls import path
from . import views

urlpatterns = [
    path('<int:activity_id>/', views.activity_detail, name='activity_detail'),
    path('<int:activity_id>/edit/', views.edit_activity, name='edit_activity'),
]
