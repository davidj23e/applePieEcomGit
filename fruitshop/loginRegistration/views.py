from django.shortcuts import render

# myapp/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm1, RegistrationForm2, ForgotPassword, ForgotPasswordEmail, LoginForm
from .models import RegistrationModel

def index(request):
    return HttpResponse("Hello, world!")

def login_view(request):
    # return HttpResponse("Hello, world2")
    if request.session.has_key('profile_user'):
        return redirect('homepage')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            email = cleaned_data['email']
            password = cleaned_data['password']
            request.session['profile_user'] = RegistrationModel.objects.get(email=email).username
            request.session['profile.email'] = RegistrationModel.objects.get(email=email).email
            return redirect('homepage')
    return render(request, 'login.html', {'form': form})

def register_page_1(request):
    form = RegistrationForm1()
    if request.method == 'POST':
        form = RegistrationForm1(request.POST)
        # Validate and save form data
        if form.is_valid():
            cleaned_data = form.cleaned_data
            request.session['username'] = cleaned_data['username']
            request.session['email'] = cleaned_data['email']
            request.session['phone'] = cleaned_data['phone']
            return redirect('register_page_2')  

    return render(request, 'formtemplate.html', {'form': form, 'buttonName' : 'Next'})

def register_page_2(request):
    print("Data", request.session['username'], request.session['email'], request.session['phone'])
    form = RegistrationForm2()
    if request.method == 'POST':
        form = RegistrationForm2(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = RegistrationModel(
                username = request.session['username'],
                email = request.session['email'],
                phone = request.session['phone'],
                password = cleaned_data['password1'],
            )
            user.save()
            request.session.flush()
            request.session.delete()
            # Save the form data
            return redirect('homepage')
            # Validate and save password
    else:
        form = RegistrationForm2()

    return render(request, 'formtemplate.html', {'form': form, 'buttonName' : 'Submit'})

def forgot_password_email(request):
    form = ForgotPasswordEmail()
    if request.method == 'POST':
        form = ForgotPasswordEmail(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            request.session['email'] = cleaned_data['email']
            # Save the form data
            return redirect('forgot_password')
            # Validate and save password
    return render(request, 'formtemplate.html', {'form': form, 'buttonName' : 'Next'})
    
def forgot_password(request):
    form = ForgotPassword(request=request)
    if request.method == 'POST':
        form = ForgotPassword(request.POST, request=request)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = RegistrationModel.objects.get(email=request.session['profile.email'])
            new_password = cleaned_data['new_password1']
            user.password=new_password
            user.save()
            # Save the form data
            return redirect('homepage')
            # Validate and save password
        else:
            print("Error Invalid form")

    return render(request, 'formtemplate.html', {'form': form, 'buttonName' : 'Submit'})

def logout(request):
    request.session.flush()
    request.session.delete()
    return redirect('homepage')

