from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/index.html')

def imupload(request):
    try:
        if request.method == 'POST':
            title = request.POST['title']
            desc = request.POST['desc']
            img = request.FILES['image']

            im = imgdb()
            im.title = title
            im.desc = desc
            im.impath = img
            im.save()
    except:
            return render(request, 'dashboard/index.html')
