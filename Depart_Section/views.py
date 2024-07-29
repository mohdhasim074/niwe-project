from django.shortcuts import render
from . models import Reserach_n_Development, Testing_and_Standards_Regulation, Departments, Wind_Resources_Assessment, Finance_and_Administration, Offshore_Wind_Development


def depart_side_tabs(request):
    return render(request, "depart-side-tabs.html")


def department_certification(request):
    return render(request, "department_certification.html")


def department_fa(request):

    fin = Finance_and_Administration.objects.all()
    if fin.exists():
        context = {"fin": fin}
    return render(request, "department_fa.html", context)


def department_fna_admin(request):
    return render(request, "department_fna_admin.html")


def department_fna_finance(request):
    return render(request, "department_fna_finance.html")


def department_fna_purchase(request):
    return render(request, "department_fna_purchase.html")


def department_owd_lidar_raw_data(request):
    return render(request, "department_owd_lidar_raw_data.html")


def department_owd(request):

    owd = Offshore_Wind_Development.objects.all().order_by('id').prefetch_related('images').order_by('id')
    if owd.exists():
        # imgObj = owd[1].images.all()
        # context = {"owd": owd, 'imgObj': imgObj}
        return render(request, "department_owd.html")


def department_rnd(request):

    RnD = Reserach_n_Development.objects.all().order_by('id')
    if RnD.exists():
        content = {'RnD': RnD}
        return render(request, "department_rnd.html", content)


def department_snr(request):

    snr = Testing_and_Standards_Regulation.objects.all()
    print(snr)
    if snr.exists():
       content = {'snr': snr}
       return render(request, "department_s&r.html", content)
    else: 
        return render(request, "department_s&r.html")

    
def department_sdt(request):
    return render(request, "department_sdt.html")


def department_srra_brief_report(request):
    return render(request, "department_srra_brief_report.html")


def department_srra_online_training(request):
    return render(request, "department_srra_online_training.html")


def department_wra(request):

    wra = Wind_Resources_Assessment.objects.all().order_by('id').prefetch_related('images').order_by('id')
    
    if wra.exists():
        # imgObj = wra[9].images.all()
        # context = {'wra': wra, 'imgObj': imgObj}
        return render(request, "department_wra.html")

# def department_wra(request):

#     wraImg = Wind_Resources_Assessment.objects.all().order_by('id').prefetch_related('images')
#     if wraImg.exists:
#         for imgObj in wraImg:
#             img = imgObj.images.all()
#             print(img)
#         context = {'wraImg': wraImg}
#         return render(request, "department_wra.html", context)

    
def department_wrao_fowind_report(request):
    return render(request, "department_wra&o_fowind_report.html")


def department_wrao_offshore_portal(request):
    return render(request, "department_wra&o_offshore_portal.html")


def departments(request):

    depart = Departments.objects.all().order_by('id')
    if depart.exists():
       context = {'depart': depart}
       return render(request, "departments.html", context)

