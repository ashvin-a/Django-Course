from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def january(request):
    return HttpResponse("To a new beginning!")

def february(request):
    return HttpResponse('Only 29 days for this month!')

def march(request):
    return HttpResponse('Summer is around the corner!')