from django.db import models
import json

class slides(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    ppt_url_1 = models.FileField(max_length=1000, default='')
    ppt_url_2 = models.FileField(max_length=1000, null=True, blank=True)
    ppt_url_3 = models.FileField(max_length=1000, null=True, blank=True)
    ppt_url_4 = models.FileField(max_length=1000, null=True, blank=True)
    ppt_url_5 = models.FileField(max_length=1000, null=True, blank=True)
    ppt_url_6 = models.FileField(max_length=1000, null=True, blank=True)

    def extension_handler(self, str):
        pos = str.rfind('.')
        ext = str[pos+1:]
        return ext


    def __str__(self):
        context = {
            'title' : self.title,
            'description' : self.description,
            'ppt_1' : {
                    'url' : str(self.ppt_url_1)+".pdf",
                    'type' : self.extension_handler(str(self.ppt_url_1))
            },
            'ppt_2' : {
                    'url' : str(self.ppt_url_2)+".pdf",
                    'type' : self.extension_handler(str(self.ppt_url_2))
            },
            'ppt_3' : {
                    'url' : str(self.ppt_url_3)+".pdf",
                    'type' : self.extension_handler(str(self.ppt_url_3))
            },
            'ppt_4' : {
                    'url' : str(self.ppt_url_4)+".pdf",
                    'type' : self.extension_handler(str(self.ppt_url_4))
            },
            'ppt_5' : {
                    'url' : str(self.ppt_url_5)+".pdf",
                    'type' : self.extension_handler(str(self.ppt_url_5))
            },
            'ppt_6' : {
                    'url' : str(self.ppt_url_6)+".pdf",
                    'type' : self.extension_handler(str(self.ppt_url_6))
            }
        }
        return json.dumps(context)
