from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import slides
from .forms import slide_upload
import json

def index(request):
    if request.method == 'POST':
        form = slide_upload(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/slide/slide_upload')
    else:
        form = slide_upload()
    return render(request, 'slideviewer/index.html', {
        'form' : form
    })

def slide_display(request):
    ppt = slides.objects.last()
    return render(request, 'slideviewer/slide_viewer.html', json.loads(str(ppt)))
