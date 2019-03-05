from django import forms

from .models import images

class image_upload_api(forms.ModelForm):
    class Meta:
        model = images
        fields = ['id',
                  'name',
                  'description',
                  'image',
                  'created_by'
                  ]
