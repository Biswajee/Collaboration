from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import imgdb
from .forms import image_upload

def index(request):
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

def imupload(request):
    context = {}
    try:
        if request.method == 'POST':
            title = request.POST['title']
            desc = request.POST['desc']
            img = request.FILES['f1']
            print(img.name)
            print(img.size)
            fs = FileSystemStorage()
            name = fs.save(img.name, img)

            # saving to database
            im = imgdb()
            im.title = title
            im.desc = desc
            im.impath = img
            im.save()

            # Saving using ModelForm


            # preparing dictionary for display
            context['url'] = fs.url(name)
            return render(request, 'dashboard/display.html', context)
    except Exception as e:
            context['error'] = str(e)
            return render(request, 'dashboard/upload_error.html', context)


def gallery_display(request):
    images = imgdb.objects.all()
    return render(request, 'dashboard/display.html', {
            'images' : images
    })
