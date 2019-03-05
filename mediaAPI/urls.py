from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.upload_image, name = 'image_api'),
    url(r'^help/', views.endpoint_list, name = 'endpoint_help'),
    url(r'^all_images/', views.Api.get_all, name = 'get_all_images'),
    url(r'^images/', views.Api.get_by_id, name = 'get_image_by_id'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
