from django.contrib import admin
from django import forms
from . models import Documents, RecordsRetentionSchedule, GeneralInformation, RevisedGuidelinesForProject, AnnualReport, ComparisonBetweenFosilFuelAndWind, FAQs, RelatedLinks

@admin.register(Documents)
class DocumentAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']

@admin.register(GeneralInformation)
class GenInfoAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']

@admin.register(ComparisonBetweenFosilFuelAndWind)
class DiffAdmin(admin.ModelAdmin):

    list_display = ('heading', 'fosil_Fuel', 'Wind_Energy')
    ordering = ['id']

@admin.register(RevisedGuidelinesForProject)
class RevisedGuidelinesAdmin(admin.ModelAdmin):

    list_display = ('sr_No', 'description', 'date')
    ordering = ['id']

@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):

    list_display = ('Year_of_Report',)
    ordering = ['id']

@admin.register(RecordsRetentionSchedule)
class RecordsRetentionScheduleAdmin(admin.ModelAdmin):

    list_display = ('ministry_Approval', 'NIEW_Records_Retention_Schedule')
    ordering = ['id']

@admin.register(RelatedLinks)
class RelatedLinksAdmin(admin.ModelAdmin):

    list_display = ('title', 'linkTitle')
    ordering = ['id']

@admin.register(FAQs)
class FaqAdmin(admin.ModelAdmin):

    list_display = ('preamble','Faq')
    ordering = ['id']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Check if the form contains the 'preamble' field before modifying it
        if 'preamble' in form.base_fields:
            if self.model.objects.exists() and not obj:
                form.base_fields['preamble'].widget = forms.HiddenInput()
        return form

    def save_model(self, request, obj, form, change):
        if not change and self.model.objects.exists():
            obj.preamble = None  # Ensure preamble is not duplicated
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if self.model.objects.exists() and not obj:
            return self.readonly_fields + ('preamble',)
        return self.readonly_fields
