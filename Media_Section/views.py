from django.http import HttpResponse
from django.shortcuts import render
from .models import Award, Gallery, Events, Citizen_Charter
def awards(request):

    award = Award.objects.all().order_by('id')
    
    if award.exists():
       return render(request, "awards.html", {'award':award})

def events(request):

    events = Events.objects.all().order_by('id')
    if events.exists():
        context = {'events': events}
        return render(request, "events.html", context)
    
def gallery(request):

    gallery = Gallery.objects.all().order_by('id')
    if gallery.exists():
       context = {'gallery': gallery}
       return render(request, "gallery.html", context)

def media(request):

    charter = Citizen_Charter.objects.first()
    if charter:
       context = {'charter': charter}
       return render(request, "media.html", context)

def charterHeader(request):

    charter = Citizen_Charter.objects.first()
    if charter:
       return HttpResponse(charter.document_File.url)

