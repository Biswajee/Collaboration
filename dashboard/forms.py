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
                  ]
