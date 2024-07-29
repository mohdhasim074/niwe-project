from django.urls import path
from . import views

urlpatterns = [
    
    path('director_general_staff/', views.about_staff, name='staff'),
    path('staff_profile_cert/', views.staff_profile_cert, name='staff_cert'),
    path('staff_profile_fa/', views.staff_profile_fa, name='staff_fin'),
    path('staff_profile_rnd/', views.staff_profile_rnd, name='staff_rnd'),
    path('staff_profile_sdt/', views.staff_profile_sdt, name='staff_sdt'),
    path('staff_profile_snr/', views.staff_profile_snr, name='staff_snr'),
    path('staff_profile_wra/', views.staff_profile_wra, name='staff_wra'),
    path('staff_profile_owd/', views.staff_profile_owd, name="staff_owd"),
]
