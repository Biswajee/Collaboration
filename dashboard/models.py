from django.db import models

class imgdb(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    impath = models.FileField

    def __str__(self):
        return self.title + '\n' + self.desc + '\n' + self.impath + '\n'        
