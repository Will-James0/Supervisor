from django.urls import path
from . import views

app_name = 'Supervisor'

urlpartterns= [
    path('', views.index, name='index')

]