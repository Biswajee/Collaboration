from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import images
from .serializers import imagesSerializer
from .forms import image_upload_api






def index(request):
    if request.method == 'POST':
        form = image_upload_api(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/api/')
    else:
        form = image_upload_api()
    return render(request, 'mediaAPI/index.html', {
        'form' : form
    })

def endpoint_list(request):
    return render(request, 'mediaAPI/endpoint_help.html')

def get_all(request):
    query_set = images.objects.all()
    serializer = imagesSerializer(query_set, many=True)
    return Response(serializer.data)
