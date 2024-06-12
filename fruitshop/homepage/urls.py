# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('addfruit', views.add_fruit, name='add_fruit'),
    path('profile_settings', views.profile_settings, name='profile_settings'),
    path('load_content', views.load_content, name='load_content'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart', views.remove_from_cart, name='remove_from_cart'),
]