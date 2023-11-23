
from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>",views.month_int),
    path("<str:month>",views.month_response)
]