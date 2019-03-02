from django.db import models
import json

class documents(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    doc_url_1 = models.FileField(max_length=1000, default='')
    doc_url_2 = models.FileField(max_length=1000, null=True, blank=True)
    doc_url_3 = models.FileField(max_length=1000, null=True, blank=True)
    doc_url_4 = models.FileField(max_length=1000, null=True, blank=True)
    doc_url_5 = models.FileField(max_length=1000, null=True, blank=True)
    doc_url_6 = models.FileField(max_length=1000, null=True, blank=True)

    def extension_handler(self, str):
        pos = str.rfind('.')
        ext = str[pos+1:]
        return ext


    def __str__(self):
        context = {
            'title' : self.title,
            'description' : self.description,
            'doc_1' : {
                    'url' : str(self.doc_url_1),
                    'type' : self.extension_handler(str(self.doc_url_1))
            },
            'doc_2' : {
                    'url' : str(self.doc_url_2),
                    'type' : self.extension_handler(str(self.doc_url_2))
            },
            'doc_3' : {
                    'url' : str(self.doc_url_3),
                    'type' : self.extension_handler(str(self.doc_url_3))
            },
            'doc_4' : {
                    'url' : str(self.doc_url_4),
                    'type' : self.extension_handler(str(self.doc_url_4))
            },
            'doc_5' : {
                    'url' : str(self.doc_url_5),
                    'type' : self.extension_handler(str(self.doc_url_5))
            },
            'doc_6' : {
                    'url' : str(self.doc_url_6),
                    'type' : self.extension_handler(str(self.doc_url_6))
            }
        }
        return json.dumps(context)
