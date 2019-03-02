from django.db import models

class documents(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    doc_url_1 = models.FileField(max_length=1000, default='')
    doc_url_2 = models.FileField(max_length=1000, null=True, blank=True)
    doc_url_3 = models.FileField(max_length=1000, null=True, blank=True)
    doc_url_4 = models.FileField(max_length=1000, null=True, blank=True)
    doc_url_5 = models.FileField(max_length=1000, null=True, blank=True)
    doc_url_6 = models.FileField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title + '\n' + self.description + '\n' + str(self.doc_url_1) + \
                '\n' + str(self.doc_url_2) + '\n' + str(self.doc_url_3) + '\n' + \
                str(self.doc_url_4) + '\n' + str(self.doc_url_5) + '\n' + str(self.doc_url_6) + '\n'
