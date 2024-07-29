from django.urls import path
from . import views

urlpatterns = [
    
    path('depart_side_tabs/', views.depart_side_tabs, name='sideTab'),
    path('department_certification/', views.department_certification, name='certificate'),
    path('department_fa/', views.department_fa, name='finance'),
    path('department_fna_admin/', views.department_fna_admin, name='admin'),
    path('department_fna_finance/', views.department_fna_finance, name='fin'),
    path('department_fna_purchase/', views.department_fna_purchase, name='purchase'),
    path('department_owd_lidar_raw_data/', views.department_owd_lidar_raw_data, name='rawData'),
    path('department_owd/', views.department_owd, name='owd'),
    path('department_rnd/', views.department_rnd, name='r&d'),
    path('department_s&r/', views.department_snr, name='s&d'),
    path('department_sdt/', views.department_sdt, name='sdt'),
    path('department_srra_brief_report/', views.department_srra_brief_report, name='report'),
    path('department_srra_online_training/', views.department_srra_online_training, name='training'),
    path('department_wra/', views.department_wra, name='wra'),
    path('department_wra&o_fowind_report/', views.department_wrao_fowind_report, name='wra&o'),
    path('department_wra&o_offshore_portal/', views.department_wrao_offshore_portal, name='portal'),
    path('departments/', views.departments, name='departments'),
    #path('department_r&d/', views.rnd, name='rnd')
]
