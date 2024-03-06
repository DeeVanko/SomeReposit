from django.urls import path
from . import views

urlpatterns = [
    path('<int:progress_id>/', views.progress_detail, name='progress_detail'),

]
