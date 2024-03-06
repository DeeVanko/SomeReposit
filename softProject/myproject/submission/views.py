from django.shortcuts import render
from .models import Submission


def submission_detail(request, submission_id):
    submission = Submission.objects.get(pk=submission_id)
    return render(request, 'submission_detail.html', {'submission': submission})
