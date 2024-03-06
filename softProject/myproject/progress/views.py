from django.shortcuts import render
from .models import Progress


def progress_detail(request, progress_id):
    progress = Progress.objects.get(pk=progress_id)
    return render(request, 'progress_detail.html', {'progress': progress})
