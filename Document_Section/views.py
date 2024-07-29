from django.shortcuts import render
from . models import Documents, RecordsRetentionSchedule, RevisedGuidelinesForProject, AnnualReport, FAQs, GeneralInformation, ComparisonBetweenFosilFuelAndWind, RelatedLinks

def download(request):

    documents = Documents.objects.all().order_by('id')
    if documents.exists():
       context = {'documents': documents}
       return render(request, "downloads.html", context)
    return render(request, "downloads.html")

def record_retention(request):

    record = RecordsRetentionSchedule.objects.all().order_by('id')
    if record.exists():
        context = {'record': record}
        return render(request, "record_retention.html", context)
    return render(request, "record_retention.html")

def relatedlinks(request):

    relLinks = RelatedLinks.objects.all().order_by('id')
    if relLinks.exists():
        context = {'relLinks': relLinks}
        return render(request, 'relatedlinks.html', context)
    return render(request, "relatedlinks.html")

def information_gi(request):

    info = GeneralInformation.objects.all().order_by('id')
    compare = ComparisonBetweenFosilFuelAndWind.objects.all().order_by('id')

    if info.exists() and compare.exists():
        context = {'info': info, 'compare': compare}
        return render(request, "information_gi.html", context) 
    return render(request, "information_gi.html")

def information_hwed(request):

    revised = RevisedGuidelinesForProject.objects.all().order_by('id')
    
    if revised.exists():
        context = {'revised': revised}
        return render(request, "information_hwed.html", context)
    return render(request, "information_hwed.html")

def faq(request):

    faqs = FAQs.objects.all().order_by('id')

    if faqs.exists():
        context = {'faqs': faqs}
        return render(request, "faq.html", context)
    return render(request, "faq.html")

def azadi_ka_amrit_mahotsav(request):

    report = AnnualReport.objects.all().order_by('id')

    if report.exists():
        context = {'report': report}
        return render(request, "azadi_ka_amrit_mahotsav.html", context)
    return render(request, "azadi_ka_amrit_mahotsav.html")