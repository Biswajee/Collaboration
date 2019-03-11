from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import imgdb
from .forms import image_upload


# returns the homepage of the application in the base url to access various features of the application
def index(request):
    return render(request, 'dashboard/entry.html')

# returns a form page for uploading images and stores responses in the form to imgdb database
# If a get request to the URL is made, a blank form is rendered
def im_upload(request):
    if request.method == 'POST':
        form = image_upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = image_upload()
    return render(request, 'dashboard/index.html', {
        'form' : form
    })

# pulls out the last entry in the imgdb database and displays the images in the "image_list/" URL
def gallery_display(request):
    images = imgdb.objects.last()
    # print(type(images))
    return render(request, 'dashboard/display.html', {
            'images' : images
    })
