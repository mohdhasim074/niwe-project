from django.db import models

class CertificationAndInformationTechnologyStaff(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

class DirectorGeneralOfficeStaff(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

class TestingStandardsAndRegulationStaff(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

class ResearchAndDevelopmentStaff(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)

class WindResourceAssessmentStaff(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    

class SkillDevelopmentAndTrainingStaff(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)

class OffshoreWindDevelopStaff(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)

class FinanceAndAdministrationStaff(models.Model):

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.CharField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)