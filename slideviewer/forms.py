from django import forms

from .models import slides

class slide_upload(forms.ModelForm):
    class Meta:
        model = documents
        fields = ['title',
                  'description',
                  'ppt_url_1',
                  'ppt_url_2',
                  'ppt_url_3',
                  'ppt_url_4',
                  'ppt_url_5',
                  'ppt_url_6']
