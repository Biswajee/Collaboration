from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import imgdb
def index(request):
    return render(request, 'dashboard/index.html')

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

            # preparing dictionary for display
            context['url'] = fs.url(name)
            return render(request, 'dashboard/display.html', context)
    except Exception as e:
            context['error'] = str(e)
            return render(request, 'dashboard/upload_error.html', context)
