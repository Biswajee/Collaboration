from django import forms

from .models import imgdb

class image_upload(forms.ModelForm):
    class Meta:
        model = imgdb
        fields = ['title',
                  'description',
                  'image_url_1',
                  'image_url_2',
                  'image_url_3',
                  'image_url_4',
                  'image_url_5',
                  'image_url_6']
