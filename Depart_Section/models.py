from django.db import models
from tinymce.models import HTMLField
# Create your models here.\

class Departments(models.Model):

    title = models.CharField()
    description = HTMLField()

class Reserach_n_Development(models.Model):

    title = models.CharField()
    description = HTMLField(null =True, blank=True)
    document_File = models.FileField(upload_to='pdf/', null=True, blank=True)

class Testing_and_Standards_Regulation(models.Model):

    title = models.CharField()
    description = HTMLField(null=True, blank=True)
    document_File = models.FileField(upload_to="pdf/", null=True, blank=True)

class Wind_Resources_Assessment(models.Model):

    title = models.CharField()
    description = HTMLField(null=True, blank=True)

class Image(models.Model):

    title = models.CharField(null=True, blank=True, default="Not Necessary")
    WRA = models.ForeignKey(Wind_Resources_Assessment, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/')

class Offshore_Wind_Development(models.Model):

    title = models.CharField(max_length=250)
    description = HTMLField()

class RelatedImage(models.Model):

    OWD = models.ForeignKey(Offshore_Wind_Development, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/')

class Finance_and_Administration(models.Model):

    description = HTMLField()
    NIWE_Pan_ARN_GST_Details = HTMLField()
    