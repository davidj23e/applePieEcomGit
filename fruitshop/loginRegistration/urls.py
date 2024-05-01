# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.login_view, name='login_view'),
    path('register_page_1', views.register_page_1, name='register_page_1'),
    path('register_page_2', views.register_page_2, name='register_page_2'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
]