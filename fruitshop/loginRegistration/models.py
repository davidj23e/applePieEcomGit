# models.py

from django.db import models

class RegistrationModel(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
