from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import slides
from .forms import slide_upload
import json
# import comtypes.client
import win32com.client
from pythoncom import CoInitialize
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PPT_ROOT = os.path.join(BASE_DIR, 'media') + "\\"



def PPTtoPDF(inputFileName, outputFileName, formatType = 32):
    CoInitialize()
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    # powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != 'pdf':
        dot_index = outputFileName.rfind(".")
        outputFileName = outputFileName[: dot_index] + ".pdf"
        print(outputFileName)
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()


def index(request):
    if request.method == 'POST':
        form = slide_upload(request.POST, request.FILES)
        converted_files = {}

        if form.is_valid():
            form.save()
            for filename, file in request.FILES.items():
                name = request.FILES[filename].name
                PPTtoPDF(PPT_ROOT + name, PPT_ROOT + name)

                time.sleep(3)   # time in seconds
            return redirect('/slide/slide_view')
    else:
        form = slide_upload()
    return render(request, 'slideviewer/index.html', {
        'form' : form
    })


def slide_display(request):
    ppt = slides.objects.last()
    return render(request, 'slideviewer/slide_viewer.html', json.loads(str(ppt)))
