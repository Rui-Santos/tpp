from django.http import HttpResponse
from django.shortcuts import render

from api.apps.gdrive.forms import TimetableForm


def upload_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Obrigado pelo upload!")
    else:
        form = TimetableForm()
    return render(request, 'timetable_upload.html', {
        'form': form
    })
