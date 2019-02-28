from django.db import models

class imgdb(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image_url_1 = models.ImageField(max_length=1000, default='')
    image_url_2 = models.ImageField(max_length=1000, null=True, blank=True)
    image_url_3 = models.ImageField(max_length=1000, null=True, blank=True)
    image_url_4 = models.ImageField(max_length=1000, null=True, blank=True)
    image_url_5 = models.ImageField(max_length=1000, null=True, blank=True)
    image_url_6 = models.ImageField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title + '\n' + self.description + '\n' + str(self.image_url_1) + \
                '\n' + str(self.image_url_2) + '\n' + str(self.image_url_3) + '\n' + \
                str(self.image_url_4) + '\n' + str(self.image_url_5) + '\n' + str(self.image_url_6) + '\n'
