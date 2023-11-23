from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

def month_response(request,month):
    text = ""
    if month=="january":
        text = "To a new beginning!"
    elif month=="february":
        text = "Only 29 days for this month!"
    elif month=="march":
        text = "Summer is around the corner"
    else:
        return HttpResponseNotFound("Ithu ninte area alla!")
    return HttpResponse(text)

def month_int(request,month):
    return HttpResponse(month)