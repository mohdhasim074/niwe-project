from django.shortcuts import render
from . models import CertificationAndInformationTechnologyStaff, FinanceAndAdministrationStaff, OffshoreWindDevelopStaff, ResearchAndDevelopmentStaff, SkillDevelopmentAndTrainingStaff, TestingStandardsAndRegulationStaff, WindResourceAssessmentStaff, DirectorGeneralOfficeStaff


def about_staff(request):

    dgStaff = DirectorGeneralOfficeStaff.objects.all().order_by('id')
    if dgStaff.exists():
       content = {'dgStaff': dgStaff}
       return render(request, "about_staff.html", content)


def staff_profile_cert(request):

    staffs = CertificationAndInformationTechnologyStaff.objects.all().order_by('id')
    if staffs.exists():
        context = {'staffs': staffs}
        return render(request, "staff_profile_cert.html", context)
    return render(request, "staff_profile_cert.html")


def staff_profile_fa(request):

    finStaff = FinanceAndAdministrationStaff.objects.all().order_by('id')
    if finStaff.exists():
        context = {'finStaff': finStaff}
        return render(request, "staff_profile_fa.html", context)
    return render(request, "staff_profile_fa.html")


def staff_profile_owd(request):

    owdStaff = OffshoreWindDevelopStaff.objects.all().order_by('id')
    if owdStaff.exists():
        context = {'owdStaff': owdStaff}
        return render(request, "staff_profile_owd.html", context)
    return render(request, "staff_profile_owd.html")


def staff_profile_rnd(request):

    rndStaff = ResearchAndDevelopmentStaff.objects.all().order_by('id')
    if rndStaff.exists():
        context = {'rndStaff': rndStaff}
        return render(request, "staff_profile_rnd.html", context)
    return render(request, "staff_profile_rnd.html")


def staff_profile_sdt(request):

    sdtStaff = SkillDevelopmentAndTrainingStaff.objects.all().order_by('id')
    if sdtStaff.exists():
        context = {'sdtStaff': sdtStaff}
        return render(request, "staff_profile_sdt.html", context)
    return render(request, "staff_profile_sdt.html")


def staff_profile_snr(request):

    snrStaff = TestingStandardsAndRegulationStaff.objects.all().order_by('id')
    if snrStaff.exists():
        context = {'snrStaff': snrStaff}
        return render(request, "staff_profile_snr.html", context)
    return render(request, "staff_profile_snr.html")


def staff_profile_wra(request):

    wraStaff = WindResourceAssessmentStaff.objects.all().order_by()
    if wraStaff.exists():
        context = {'wraStaff': wraStaff}
        return render(request, "staff_profile_wra.html", context)
    return render(request, "staff_profile_wra.html")

