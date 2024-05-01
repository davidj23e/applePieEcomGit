from django.shortcuts import render

# myapp/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm1, RegistrationForm2, ForgotPassword

def index(request):
    return HttpResponse("Hello, world!")

def login_view(request):
    # return HttpResponse("Hello, world2")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def register_page_1(request):
    form = RegistrationForm1()
    if request.method == 'POST':
        form = RegistrationForm1(request.POST)
        # Validate and save form data
        
        return redirect('register_page_2')  

    return render(request, 'formtemplate.html', {'form': form})

def register_page_2(request):
    form = RegistrationForm2()
    if request.method == 'POST':
        form = RegistrationForm2(request.POST)
        # Validate and save password
        
        return redirect('home')

    return render(request, 'formtemplate.html', {'form': form})

def forgot_password(request):
    form = ForgotPassword()
    if request.method == 'POST':
        form = ForgotPassword(request.POST)
        # Validate and save password
        
        return redirect('home')

    return render(request, 'formtemplate.html', {'form': form})


