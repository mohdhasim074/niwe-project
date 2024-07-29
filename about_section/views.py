from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import AboutUs, DirectorGeneralMessage, Background, charter, OrganizationalChart, QualityPolicy


def about_us(request):

    aboutUs = AboutUs.objects.all()
    if aboutUs.exists():
      content = {'aboutUs': aboutUs}
      return render(request, "about_us.html", content)


def about_background(request):

    background = Background.objects.all()
    if background.exists():
       content = {'background': background}
       return render(request, "about_background.html", content)


def about_charter(request):

    chart = charter.objects.all()
    if chart.exists():
        content = {'chart': chart}
        return render(request, "about_charter.html", content)


def about_dgm(request):

    dgm = DirectorGeneralMessage.objects.all()
    if dgm.exists():
      content = {'dgm': dgm}
      return render(request, "about_dgm.html", content)


def about_org(request):

    org = OrganizationalChart.objects.all()
    if org.exists():
      content = {'org': org}
      return render(request, "about_org.html", content)


def about_qlty_ply(request):

    quality = QualityPolicy.objects.all()
    if quality.exists():
       content = {'quality': quality}
       return render(request, "about_qlty_ply.html", content)

# def about_staff(request):

#     dgStaff = dgStaff.objects.all()
#     if about_staff.exists():
#        content = {'staff': dgStaff}
#        return render(request, "about_staff.html", content)

