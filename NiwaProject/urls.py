"""
URL configuration for NiwaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', views.index),
    path('about/', include('about_section.urls')),
    path('media/', include('Media_Section.urls')),
    path('department/', include('Depart_Section.urls')),
    path('downloads/', include('Document_Section.urls')),
    path('contact/', include('Contact_Us.urls')),
    path('staff/', include('Staff_Section.urls'), name='search'),
    path('', include('Right_To_Information.urls')),
    path('careers/', include('Career_Section.urls')),
    # path('about_background/', views.about_background),
    # path('about_charter/', views.about_charter),
    # path('about_dgm/', views.about_dgm),
    # path('about_org/', views.about_org),
    # path('about_qlty_ply/', views.about_qlty_ply),
    # path('about_staff/', views.about_staff),
    # path('about_us/', views.about_us),
    path('audit_report/', views.audit_report, name='audit'),
    path('annual_account/', views.annual_account, name='account'),
    path('akam_2022_23_event1/', views.akam_2022_23_event1, name='akam_2022_23_event1'),
    path('amrit_mahotsav_22_23/', views.amrit_mahotsav_22_23, name='amrit_mahotsav_22_23'),
    # path('awards/', views.awards),
    # path('azadi_ka_amrit_mahotsav/', views.azadi_ka_amrit_mahotsav, name='azadi_ka_amrit_mahotsav'),
    # path('careers/', views.careers),
    # path('contact/', views.contact),
    # path('depart_side_tabs/', views.depart_side_tabs),
    # path('department_certification/', views.department_certification),
    # path('department_fa/', views.department_fa),
    # path('department_fna_admin/', views.department_fna_admin),
    # path('department_fna_finance/', views.department_fna_finance),
    # path('department_fna_purchase/', views.department_fna_purchase),
    # path('department_owd_lidar_raw_data/', views.department_owd_lidar_raw_data),
    # path('department_owd/', views.department_owd),
    # path('department_rnd/', views.department_rnd),
    # path('department_s&r/', views.department_s_r),
    # path('department_sdt/', views.department_sdt),
    # path('department_srra_brief_report/', views.department_srra_brief_report),
    path('department_srra_online_training/', views.department_srra_online_training, name='department_srra_online_training'),
    # path('department_wra/', views.department_wra),
    # path('department_wra&o_fowind_report/', views.department_wrao_fowind_report),
    # path('department_wra&o_offshore_portal/', views.department_wrao_offshore_portal),
    # path('departments/', views.departments),
    # path('downloads/', views.downloads),
    # path('events/', views.events),
    # path('faq/', views.faq),
    path('fowpi_workshop_presentation/', views.fowpi_workshop_presentation),
    # path('gallery/', views.gallery),
    # path('information_gi/', views.information_gi),
    # path('information_hwed/', views.information_hwed),
    path('information_weg_installation/', views.information_weg_installation),
    path('international_conference_wsra/', views.international_conference_wsra, name='international_conference_wsra'),
    path('international_workshop_ppt/', views.international_workshop_ppt, name='international_workshop_ppt'),
    path('ireda_niwe_annual_awards/', views.ireda_niwe_annual_awards, name='ireda_niwe_annual_awards'),
    # path('media/', views.media),
    path('offshore_EPD_Gujarat/', views.offshore_EPD_Gujarat),
    path('pan-india_workshop/', views.pan_india_workshop, name='pan-india_workshop'),
    # path('record_retention/', views.record_retention),
    # path('relatedlinks/', views.relatedlinks),
    # path('rti/', views.rti),
    path('services/', views.services),
    path('small_wind_energy_&_hybrid_system_presentation/', views.small_wind_energy_hybrid_system_presentation, name='swe&hsp'),
    # path('staff_profile_cert/', views.staff_profile_cert),
    # path('staff_profile_fa/', views.staff_profile_fa),
    # path('staff_profile_rnd/', views.staff_profile_rnd),
    # path('staff_profile_sdt/', views.staff_profile_sdt),
    # path('staff_profile_snr/', views.staff_profile_snr),
    # path('staff_profile_wra/', views.staff_profile_wra),
    # path('staff_profile_owd/', views.staff_profile_owd),
    path('sub-gallery/', views.sub_gallery, name='sub-gallery'),
    path('tenders/', views.tenders),
    path('wind_potential/', views.wind_potential),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
