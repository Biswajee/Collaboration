import os
import time

# import comtypes.client
import win32com.client
from django.shortcuts import redirect, render
from pythoncom import CoInitialize

from .forms import slide_upload
from .models import slide_files, slides

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PPT_ROOT = os.path.join(BASE_DIR, "media") + "\\"


def PPTtoPDF(inputFileName, outputFileName, formatType=32):
    CoInitialize()
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    # powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != "pdf":
        outputFileName = outputFileName + ".pdf"
        print(outputFileName)
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType)  # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()


def index(request):
    if request.method == "POST":
        form = slide_upload(request.POST, request.FILES)

        if form.is_valid():
            saveRes = form.save()
            for file in request.FILES.getlist("slide"):
                saveSlides = slide_files(sequence=saveRes, slide_urls=file)
                saveSlides.save()

                # convert each presentation files to pdf format
                PPTtoPDF(PPT_ROOT + str(file), PPT_ROOT + str(file))

            time.sleep(10)  # time in seconds
            return redirect("/slide/slide_view")
    else:
        form = slide_upload()
    return render(request, "slideviewer/index.html", {"form": form})


def slide_display(request):
    presentation = slides.objects.last()
    presentation_files = slide_files.objects.filter(sequence=presentation.id)

    context = []
    for file in presentation_files:
        context.append(file)
    return render(
        request,
        "slideviewer/slide_viewer.html",
        {
            "slide_files": context,
            "title": presentation.title,
            "description": presentation.description,
        },
    )
