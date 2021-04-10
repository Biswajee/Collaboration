from django import forms

from .models import slides


class slide_upload(forms.ModelForm):
    class Meta:
        model = slides
        fields = [
            "title",
            "description",
        ]
