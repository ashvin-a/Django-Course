
from django.urls import path
from . import views

urlpatterns = [
    path("",views.show_months),
    path("<int:month>",views.month_int),
    path("<str:month>",views.month_res,name="month_name")
]