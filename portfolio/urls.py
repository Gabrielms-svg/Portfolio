"""
URL configuration for portfolio project.
"""
from django.contrib import admin
from django.urls import path

from home.views import home_view
from projects.views import (
    project_cams_view,
    project_sysmon_view,
    project_waste_detect_view,
    projects_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('projects/', projects_view, name='projects'),
    path('projects/waste-detect/', project_waste_detect_view, name='project_waste_detect'),
    path('projects/cams/', project_cams_view, name='project_cams'),
    path('projects/sysmon/', project_sysmon_view, name='project_sysmon'),
]
