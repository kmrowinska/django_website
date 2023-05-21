from django.urls import path
from . import views

app_name = 'covid19'

urlpatterns = [
    path('', views.covid_view, name="COVID-19"),
    path('<code>/', views.covid_view_cn, name="COVID-19"),

]