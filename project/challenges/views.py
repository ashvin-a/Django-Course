from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
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
        res = month_response[month]
    except:
        return HttpResponseNotFound("Ithu ninte area allaa!!")
    return render(request,"challenges/challenge.html",{"month":month.capitalize(),"challenge":res})

def month_int(request,month):
    if 0<month<13:
        months = list(month_response.keys())
        text = months[month-1]
        ftext = reverse("month_name",args=[text])#month_num is mentioned in 
        #urls.py. ftext = /challenges/month. we can change urls in urls.py 
        # of main as well
    else:
        return HttpResponseNotFound("There are only 12 months!!")
    
    return HttpResponseRedirect(ftext)

def show_months(request):
    l=list(month_response.keys())
    #use render instead of render_to_string
    return render(request,"challenges/index.html",{"months":l}) #month variable in challenge.html

        
    