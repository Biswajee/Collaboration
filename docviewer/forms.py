from django import forms

from .models import documents


class doc_upload(forms.ModelForm):
    class Meta:
        model = documents
        fields = [
            "title",
            "description",
        ]
