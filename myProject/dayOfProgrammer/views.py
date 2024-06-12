from datetime import date, timedelta
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def programmer_day(request):
    current_year = date.today().year
    programmer_date = date(current_year, 1, 1) + timedelta(days=255)
    return HttpResponse(f"День программиста в этом году: \
{programmer_date.strftime("%d/%m/%Y")}")