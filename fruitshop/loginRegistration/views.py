from django.shortcuts import render

# myapp/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
