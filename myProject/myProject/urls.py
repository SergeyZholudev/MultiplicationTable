"""
URL configuration for myProject project.

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
from django.urls import path
from django.urls import re_path

from CurrentDate.views import date_time
from django.views.generic import TemplateView
from dayOfProgrammer.views import programmer_day

urlpatterns = [
    re_path(r'^prog', programmer_day),
    re_path(r'^date', date_time),
    re_path(r'^mult', TemplateView.as_view(template_name="MultiplicationTable.html")),
    path('admin/', admin.site.urls),
    path('', date_time),
]
