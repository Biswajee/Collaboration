from rest_framework import serializers

from .models import images


class imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = images
        fields = '__all__'
