
from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>",views.month_int,name="month_num"),
    path("<str:month>",views.month_res)
]