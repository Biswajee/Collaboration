import json

from django.db import models


class images(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='ImageAPI', max_length=1000)
    created_by = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + "\n" + self.name + "\n" + self.description + "\n" + str(self.image) + "\n" + self.created_by

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
