from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import documents
from .forms import doc_upload
import json

# returns the form page to upload documents, for get request, returns blank form page
def index(request):
    if request.method == 'POST':
        form = doc_upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/doc/doc_view')
    else:
        form = doc_upload()
    return render(request, 'docviewer/index.html', {
        'form' : form
    })

# returns a display of documents by extracting last entry in the database after form is sumbitted
def doc_display(request):
    docx = documents.objects.last()
    return render(request, 'docviewer/document_viewer.html', json.loads(str(docx)))
