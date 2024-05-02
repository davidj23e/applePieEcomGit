from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import FruitInventoryForm
from .models import FruitInventory

# Create your views here.
def homepage(request):
    fruits = FruitInventory.objects.all()
    if request.session.has_key('profile.user'):
        user = request.session['profile.user']
    else:
        user = None
    return render(request, 'homebase.html', {'fruits': fruits, 'username': user})
    # return HttpResponse("HOMEPAGE PLACEHOLDER")
    

def add_fruit(request):
    form = FruitInventoryForm()
    buttonName = "Add Fruit"
    if request.method == 'POST':
        form = FruitInventoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fruit added successfully')
            return redirect('add_fruit')
            
    return render(request, 'formtemplate.html', {'form': form, 'buttonName' : buttonName})
