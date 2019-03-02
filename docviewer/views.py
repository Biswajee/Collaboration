from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import documents
from .forms import doc_upload

def index(request):
    if request.method == 'POST':
        form = doc_upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doc_view')
    else:
        form = doc_upload()
    return render(request, 'docviewer/index.html', {
        'form' : form
    })

def gallery_display(request):
    docx = documents.objects.last()
    return render(request, 'dashboard/document_viewer.html', {
            'documents' : docx
    })
