from django import forms

from .models import documents

class doc_upload(forms.ModelForm):
    class Meta:
        model = documents
        fields = ['title',
                  'description',
                  'doc_url_1',
                  'doc_url_2',
                  'doc_url_3',
                  'doc_url_4',
                  'doc_url_5',
                  'doc_url_6']
