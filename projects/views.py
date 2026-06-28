from django.shortcuts import render


def projects_view(request):
    return render(request, 'projects.html')


def project_waste_detect_view(request):
    return render(request, 'project_waste_detect.html')


def project_cams_view(request):
    return render(request, 'project_cams.html')


def project_sysmon_view(request):
    return render(request, 'project_sysmon.html')
