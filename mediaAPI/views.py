from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import images
from .forms import image_upload_api
import json

def index(request):
    if request.method == 'POST':
        form = image_upload_api(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/api/')
    else:
        form = image_upload_api()
    return render(request, 'mediaAPI/index.html', {
        'form' : form
    })

def endpoint_list(request):
    docx = documents.objects.last()
    return render(request, 'mediaAPI/endpoint_help.html', json.loads(str(docx)))
