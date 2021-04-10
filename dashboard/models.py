from django.db import models


class imgdb(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title + "\n" + self.description


class img_files(models.Model):
    sequence = models.ForeignKey(imgdb, on_delete=models.CASCADE)
    img_urls = models.ImageField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.img_urls)
