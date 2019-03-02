from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import imgdb
from .forms import image_upload

def index(request):
    return render(request, 'dashboard/entry.html')

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

def gallery_display(request):
    images = imgdb.objects.last()
    print(type(images))
    return render(request, 'dashboard/display.html', {
            'images' : images
    })
