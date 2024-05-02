# models.py

from django.db import models

class FruitInventory(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=5, decimal_places=2) 
    tagline = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fruit_images/')

    def __str__(self):
        return self.item_name
