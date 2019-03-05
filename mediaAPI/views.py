from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import images
from .serializers import imagesSerializer
from .forms import image_upload_api



def upload_image(request):
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


# Core API features
class Api(APIView):
    def get_all(request):
        query_set = list(images.objects.all().values())
        print(query_set)
        if len(query_set) == 0:
            context = {'error' : 'no entries present in database'}
            return JsonResponse(context)
        else:
            return JsonResponse(query_set, safe=False)


    def get_by_id(request):
        query = request.GET.get('id')

        if query == None:
            context = {
                'error': 'You need to pass in parameters'
            }
            return JsonResponse(context)
        else:
            query_set = images.objects.get(id=query)
            context = {
                'id' : query,
                'url' : "http://127.0.0.1:8000/media/" + str(query_set.image)
            }
            return JsonResponse(context)
