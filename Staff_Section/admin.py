from django.contrib import admin
from .models import CertificationAndInformationTechnologyStaff, ResearchAndDevelopmentStaff, WindResourceAssessmentStaff, OffshoreWindDevelopStaff, TestingStandardsAndRegulationStaff, FinanceAndAdministrationStaff, SkillDevelopmentAndTrainingStaff, DirectorGeneralOfficeStaff

@admin.register(CertificationAndInformationTechnologyStaff)
class CnITStaff(admin.ModelAdmin):

     list_display = ('name', 'position', 'email', 'phone_number', 'department')
     list_filter = ('department',)
     ordering = ['id']

class DGStaffAdmin(admin.ModelAdmin):

    list_display = ('name', 'position', 'email', 'phone_number')
    list_filter = ('position',)
    ordering = ['id']

admin.site.register(DirectorGeneralOfficeStaff, DGStaffAdmin)

@admin.register(ResearchAndDevelopmentStaff)
class RnDStaff(admin.ModelAdmin):

     list_display = ('name', 'position', 'email', 'phone_number')
     ordering = ['id']

@admin.register(WindResourceAssessmentStaff)
class WRAStaff(admin.ModelAdmin):

     list_display = ('name', 'position', 'email', 'phone_number')
     ordering = ['id']

@admin.register(OffshoreWindDevelopStaff)
class OWDStaff(admin.ModelAdmin):

     list_display = ('name', 'position', 'email', 'phone_number')
     ordering = ['id']

@admin.register(TestingStandardsAndRegulationStaff)
class Test_StandRegulation_Staff(admin.ModelAdmin):

     list_display = ('name', 'position', 'email', 'phone_number', 'department')
     list_filter = ('department',)
     ordering = ['id']

@admin.register(FinanceAndAdministrationStaff)
class FnAStaff(admin.ModelAdmin):

     list_display = ('name', 'position', 'email', 'phone_number', 'department')
     list_filter = ('department',)
     ordering = ['id']

@admin.register(SkillDevelopmentAndTrainingStaff)
class SDTStaff(admin.ModelAdmin):

     list_display = ('name', 'position', 'email', 'phone_number')
     ordering = ['id']