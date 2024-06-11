from datetime import datetime

from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def date_time(request):
    currentDate = datetime.now()
    return HttpResponse(currentDate)
