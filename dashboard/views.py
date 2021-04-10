from django.shortcuts import redirect, render

from .forms import image_upload
from .models import img_files, imgdb


# returns the homepage of the application in the base url to access various features of the application
def index(request):
    return render(request, "dashboard/entry.html")


# returns a form page for uploading images and stores responses in the form to imgdb database
# If a get request to the URL is made, a blank form is rendered
def im_upload(request):
    if request.method == "POST":
        form = image_upload(request.POST)
        if form.is_valid():
            saveRes = form.save()

            for file in request.FILES.getlist("file"):
                image_files = img_files(sequence=saveRes, img_urls=file)
                image_files.save()
            return redirect("image_list")
    else:
        form = image_upload()
    return render(request, "dashboard/index.html", {"form": form})


# pulls out the last entry in the imgdb database and displays the images in the "image_list/" URL
def gallery_display(request):
    images = imgdb.objects.last()
    image_files = img_files.objects.filter(sequence=images.id)
    context = []
    for file in image_files:
        context.append(file)

    return render(
        request,
        "dashboard/display.html",
        {
            "image_files": context,
            "title": images.title,
            "description": images.description,
        },
    )
