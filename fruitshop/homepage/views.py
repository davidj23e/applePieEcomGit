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

def profile_settings(request):
    if request.session.has_key('profile.user'):
        user = request.session['profile.user']
    else:
        user = None
    return render(request, 'profile_settings.html', {'username': user})

def load_content(request):
    target = request.GET.get('target')
    if target == 'content1':
        content = '<h1>Content 1</h1><p>This is the content for Content 1.</p>'
    elif target == 'content2':
        content = '<h1>Content 2</h1><p>This is the content for Content 2.</p>'
    elif target == 'content3':
        content = '<h1>Content 3</h1><p>{{ username }}</p>'
    else:
        content = '<p>No content found.</p>'
    return render(request, 'content.html', {'content': content})
