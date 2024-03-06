from django.shortcuts import render
from .models import Activity


def activity_detail(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    return render(request, 'activity_detail.html', {'activity': activity})


def edit_activity(request, activity_id):
    # Logic to edit activity
    pass
