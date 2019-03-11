from django import forms

from .models import imgdb

'''
image_upload form renders on the index.html for image upload service
and stores associated data to the imgdb database described in the models.py
'''


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
