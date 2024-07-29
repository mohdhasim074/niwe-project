from django.contrib import admin
from .models import Departments, Reserach_n_Development, Testing_and_Standards_Regulation, Wind_Resources_Assessment, Image, Offshore_Wind_Development, RelatedImage, Finance_and_Administration

class ImageInline(admin.StackedInline):

   model = Image
    
@admin.register(Departments)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']

@admin.register(Reserach_n_Development)
class RnDAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'document_File')
    ordering = ['id']

@admin.register(Testing_and_Standards_Regulation)
class TestingAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'document_File')
    ordering = ['id']

@admin.register(Wind_Resources_Assessment)
class Wind_Res_Admin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']
    inlines = [ImageInline]

class RelatedImageInline(admin.StackedInline):

    model = RelatedImage

@admin.register(Offshore_Wind_Development)
class OwdAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']
    inlines = [RelatedImageInline]

@admin.register(Finance_and_Administration)
class FnAdmin(admin.ModelAdmin):

    list_display = ('description', 'NIWE_Pan_ARN_GST_Details')
    
