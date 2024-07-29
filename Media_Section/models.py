from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html

class Award(models.Model):

     title = models.CharField()
     description = HTMLField()
     image_1 = models.FileField(upload_to='images/', null=True, blank=True)
     image_2 = models.FileField(upload_to='images/', null=True, blank=True)

     def image_Tag(self):
          return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;" />'.format(self.image_1))
     
     image_Tag.short_description = 'Image'
class Gallery(models.Model):

     title = models.CharField(max_length=100)
     image = models.ImageField(upload_to="images/", default=None)

     def image_Tag(self):
          return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"/>'.format(self.image))

     image_Tag.short_description = 'Image'     

class Citizen_Charter(models.Model):
     
     title = models.CharField(default="Citizen Charter")
     document_File = models.FileField(upload_to='pdf/', max_length=100)

class Events(models.Model):

     title = models.CharField()
     document_File = models.FileField(upload_to='pdf/', max_length=100, blank=True)
     url = models.URLField(blank=True, null=True, default="Empty")
