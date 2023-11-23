from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

month_response = {
    "january":"To a new beginning",
    "february":"Only 28 days in this month",
    "march":"Summer is around the corner",
    "april":"Fools day",
    "may":"May Day Holiday",
    "june":"Meh this is getting boring",
    "july":"Yeah its definetly getting boring",
    "august":"Leo was born",
    "september":"Its about damn time we take on a challenge",
    "october":"Lets hit gym all day",
    "november":"#NNN",
    "december":"Jingle bells are on the way"
}

def month_res(request,month):
    try:
        text = month_response[month]
    except:
        return HttpResponseNotFound("Ithu ninte area allaa!!")
    return HttpResponse(text)

