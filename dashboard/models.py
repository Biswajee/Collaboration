from django.db import models

class imgdb(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image_url = models.FileField(max_length=1000, default='')

    def __str__(self):
        return self.title + '\n' + self.desc + '\n' + self.impath + '\n'
