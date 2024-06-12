from django import forms
from django.core.exceptions import ValidationError
from .models import RegistrationModel
import re

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        
        try:
            user = RegistrationModel.objects.get(email=email)
        except RegistrationModel.DoesNotExist:
            raise forms.ValidationError("Email does not exist")
        
        print(user.password, password)
        if not user.password == password:
            raise forms.ValidationError("Incorrect password")

class RegistrationForm1(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        
        if email in RegistrationModel.objects.values_list('email', flat=True):
            raise forms.ValidationError("Email already exists")
        if phone in RegistrationModel.objects.values_list('phone', flat=True):
            raise forms.ValidationError("Phone number already exists")

class RegistrationForm2(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        if re.search(r'\d', password1) is None:
            raise ValidationError("Password must contain at least 1 number")
        if re.search(r'[A-Z]', password1) is None: 
            raise ValidationError("Password must contain at least 1 uppercase letter")
        if re.search(r'[!@#$%^&*()]', password1) is None:
            raise ValidationError("Password must contain at least 1 special character")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    
class ForgotPasswordEmail(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned = super().clean()
        email = cleaned.get("email")
        if email not in (RegistrationModel.objects.values_list('email', flat=True)):
            raise forms.ValidationError("User with the Email does not exist")

class ForgotPassword(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request') 
        super(ForgotPassword, self).__init__(*args, **kwargs)
    
    def clean(self):
        email = self.request.session.get('profile.email')
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")
        
        try:
            temp = RegistrationModel.objects.get(email=email).password
        except RegistrationModel.DoesNotExist:
            raise forms.ValidationError("The old password is incorrect")
        # if old_password not in RegistrationModel.objects.get(email=email).password:
        #     raise forms.ValidationError("The old password is incorrect")

        if len(new_password1) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        if re.search(r'\d', new_password1) is None:
            raise ValidationError("Password must contain at least 1 number")
        if re.search(r'[A-Z]', new_password1) is None: 
            raise ValidationError("Password must contain at least 1 uppercase letter")
        if re.search(r'[!@#$%^&*()]', new_password1) is None:
            raise ValidationError("Password must contain at least 1 special character")
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("New Passwords do not match")

        return cleaned_data