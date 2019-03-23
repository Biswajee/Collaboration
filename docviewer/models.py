from django.db import models
import json

class documents(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


    def extension_handler(self, str):
        pos = str.rfind('.')
        ext = str[pos+1:]
        return ext


    def __str__(self):
        context = {
            'id' : self.id,
            'title' : self.title,
            'description' : self.description,
        }
        return json.dumps(context)

class document_files(models.Model):
     sequence = models.ForeignKey(documents , on_delete=models.CASCADE)
     doc_urls = models.FileField(max_length=1000, null=True, blank=True)


     def __str__(self):
         return str(self.doc_urls)
