from django.http import HttpResponse
from django.shortcuts import render, redirect
from about_section.models import DirectorGeneralMessage


def index(request):
    dgm = DirectorGeneralMessage.objects.all()
    if dgm.exists:
      return render(request, "index.html", {'dgm': dgm})


def audit_report(request):
    return render(request, "audit_report.html")


def annual_account(request):
    return render(request, "annual_accounts.html")
# def about_background(request):
#     return render(request, "about_background.html")

# def about_charter(request):
#     return render(request, "about_charter.html")

# def about_dgm(request):
#     return render(request, "about_dgm.html")

# def about_org(request):
#     return render(request, "about_org.html")

# def about_qlty_ply(request):
#     return render(request, "about_qlty_ply.html")

# def about_staff(request):
#     return render(request, "about_staff.html")

# def about_us(request):
#     return render(request, "about_us.html")


def akam_2022_23_event1(request):
    return render(request, "akam_2022-23_event1.html")


def amrit_mahotsav_22_23(request):
    return render(request, "amrit-mahotsav-22-23.html")

# def awards(request):
#     return render(request, "awards.html")

# def azadi_ka_amrit_mahotsav(request):
#     return render(request, "azadi_ka_amrit_mahotsav.html")

# def careers(request):
#     return render(request, "careers.html")

# def contact(request):
#     return render(request, "contact.html")

# def depart_side_tabs(request):
#     return render(request, "depart-side-tabs.html")

# def department_certification(request):
#     return render(request, "department_certification.html")

# def department_fa(request):
#     return render(request, "department_fa.html")

# def department_fna_admin(request):
#     return render(request, "department_fna_admin.html")

# def department_fna_finance(request):
#     return render(request, "department_fna_finance.html")

# def department_fna_purchase(request):
#     return render(request, "department_fna_purchase.html")

# def department_owd_lidar_raw_data(request):
#     return render(request, "department_owd_lidar_raw_data.html")

# def department_owd(request):
#     return render(request, "department_owd.html")

# def department_rnd(request):
#     return render(request, "department_rnd.html")

# def department_s_r(request):
#     return render(request, "department_s&r.html")
    
# def department_sdt(request):
#     return render(request, "department_sdt.html")

# def department_srra_brief_report(request):
#     return render(request, "department_srra_brief_report.html")


def department_srra_online_training(request):
      return render(request, "department_srra_online_training.html")

# def department_wra(request):
#     return render(request, "department_wra.html")

# def department_wrao_fowind_report(request):
#     return render(request, "department_wra&o_fowind_report.html")

# def department_wrao_offshore_portal(request):
#     return render(request, "department_wra&o_offshore_portal.html")

# def departments(request):
#     return render(request, "departments.html")

# def downloads(request):
#     return render(request, "downloads.html")

# def events(request):
#     return render(request, "events.html")

# def faq(request):
#     return render(request, "faq.html")


def fowpi_report(request):
    return render(request, "fowpi_report.html")


def fowpi_workshop_presentation(request):
    return render(request, "fowpi_workshop_presentation.html")


def gallery(request):
    return render(request, "gallery.html")

# def information_gi(request):
#     return render(request, "information_gi.html")

# def information_hwed(request):
#     return render(request, "information_hwed.html")


def information_weg_installation(request):
    return render(request, "information_weg_installation.html")


def international_conference_wsra(request):
    return render(request, "international_conference_wsra.html")


def international_workshop_ppt(request):
    return render(request, "international_workshop_ppt.html")


def ireda_niwe_annual_awards(request):
    return render(request, "ireda_niwe_annual_awards.html")

# def media(request):
#     return render(request, "media.html")


def offshore_EPD_Gujarat(request):
    return render(request, "offshore_EPD_Gujarat.html")


def pan_india_workshop(request):
    return render(request, "pan-india_workshop.html")

# def record_retention(request):
#     return render(request, "record_retention.html")

# def relatedlinks(request):
#     return render(request, "relatedlinks.html")

# def rti(request):
#     return render(request, "rti.html")


def services(request):
    return render(request, "services.html")


def small_wind_energy_hybrid_system_presentation(request):
    return render(request, "small_wind_energy_&_hybrid_system_presentation.html")

# def staff_profile_cert(request):
#     return render(request, "staff_profile_cert.html")

# def staff_profile_fa(request):
#     return render(request, "staff_profile_fa.html")

# def staff_profile_owd(request):
#     return render(request, "staff_profile_owd.html")

# def staff_profile_rnd(request):
#     return render(request, "staff_profile_rnd.html")

# def staff_profile_sdt(request):
#     return render(request, "staff_profile_sdt.html")

# def staff_profile_snr(request):
#     return render(request, "staff_profile_snr.html")

# def staff_profile_wra(request):
#     return render(request, "staff_profile_wra.html")


def sub_gallery(request):
    return render(request, "sub-gallery.html")


def tenders(request):
    return render(request, "tenders.html")


def wind_potential(request):
    return render(request, "wind_potential.html")
