from django import forms

from .models import imgdb

class image_upload(forms.ModelForm):
    class Meta:
        model = imgdb
        fields = ['title', 'description', 'image']
