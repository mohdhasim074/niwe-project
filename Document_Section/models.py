from django.db import models
from tinymce.models import HTMLField

class Documents(models.Model):

    title = models.CharField(max_length=250)
    description = HTMLField()

class GeneralInformation(models.Model):

    title = models.CharField(max_length=250)
    description = HTMLField()

class ComparisonBetweenFosilFuelAndWind(models.Model):

    heading = models.CharField()
    fosil_Fuel = HTMLField()
    Wind_Energy = HTMLField()

class RevisedGuidelinesForProject(models.Model):
     
     sr_No = models.IntegerField()
     description = HTMLField()
     date = models.DateField(auto_now=False, auto_now_add=False)

class AnnualReport(models.Model):
     
     Year_of_Report = models.CharField()

class RecordsRetentionSchedule(models.Model):
     
     ministry_Approval = models.FileField(upload_to='pdf/')
     NIEW_Records_Retention_Schedule = models.FileField(upload_to='pdf/')

class RelatedLinks(models.Model):

     title = models.CharField()
     linkTitle = HTMLField()

class FAQs(models.Model):
     
     preamble = HTMLField(null=True, blank=True)
     Faq = HTMLField()
