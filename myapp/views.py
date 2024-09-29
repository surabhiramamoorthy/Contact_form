from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def current_date_time(request):
    now=datetime.datetime.now()
    html="<html><head><h1>It is now %s.</h1>"%(now)
    return HttpResponse(html)

def four_hours_ahead(request):
    dt=datetime.datetime.now()+datetime.timedelta(hours=4)
    html="<html><head><h1>It will be %s in 4 hours.</h1>"%(dt)
    return HttpResponse(html)

def four_hours_before(request):
    dt=datetime.datetime.now()+datetime.timedelta(hours=-4)
    html="<html><head><h1>It was %s before 4 hours.</h1>"%(dt)
    return HttpResponse(html)
