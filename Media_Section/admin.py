from django.contrib import admin
from .models import Award, Gallery, Citizen_Charter, Events

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'image_Tag')
    ordering = ['id']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = ('title', 'image_Tag')
    ordering = ['id']

@admin.register(Citizen_Charter)
class Citi_Chart_Admin(admin.ModelAdmin):

    list_display = ('title','document_File') 

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):

    list_display = ('title', 'document_File', 'url')
    ordering = ['id']