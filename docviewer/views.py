import json

from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render

from .forms import doc_upload
from .models import document_files, documents

# returns the form page to upload documents, for get request, returns blank form page
# index() accepts form data and saves it into two tables, namely documents and document_files.
# The document saves the title and description of the file with a unique id, this id is used
# in the document_files table to associate multiple uploaded files [foreign key].

def index(request):
    if request.method == 'POST':
        form = doc_upload(request.POST, request.FILES)
        if form.is_valid():
            saveRes = form.save()

            for file in request.FILES.getlist('file'):
                doc_files = document_files(sequence = saveRes, doc_urls = file)
                doc_files.save()
            return redirect('/doc/doc_view')
    else:
        form = doc_upload()
    return render(request, 'docviewer/index.html', {
        'form' : form
    })


# returns a display of documents by extracting last entry in the database after form is sumbitted
# doc_display() retrieves the last id value from the documents table and finds the file names corresponding
# to the id in documrnt_files table, and fills up the list (context) and sends it to the template !

def doc_display(request):
    docx = documents.objects.last()
    doc_files = document_files.objects.filter(sequence = docx.id)
    context = []
    for file in doc_files:
        context.append(file)
    return render(request, 'docviewer/document_viewer.html', {'doc_files' : context,
                                                              'title' : docx.title,
                                                              'description' : docx.description
                                                              })
