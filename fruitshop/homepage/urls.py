# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('addfruit', views.add_fruit, name='add_fruit'),
]