from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import documents
from .forms import doc_upload
import json

def index(request):
    if request.method == 'POST':
        form = doc_upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/doc/doc_upload')
    else:
        form = doc_upload()
    return render(request, 'docviewer/index.html', {
        'form' : form
    })

def doc_display(request):
    docx = documents.objects.last()
    return render(request, 'docviewer/document_viewer.html', json.loads(str(docx)))
