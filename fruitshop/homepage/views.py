from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import FruitInventoryForm
from .models import FruitInventory, UserCart

# Create your views here.
def homepage(request):
    fruits = FruitInventory.objects.all()
    if request.session.has_key('profile.user'):
        user = request.session['profile.user']
        totalOrders = UserCart.objects.filter(email=request.session['profile.email']).count()
    else:
        user = None
    return render(request, 'homebase.html', {'fruits': fruits, 'username': user, 'totalOrders': totalOrders})
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

def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('parameter')
        print(item_name)
        order, created = UserCart.objects.get_or_create(
            email=request.session['profile.email'],
            item_name=item_name,
            defaults={'quantity':1}
            )
        
        if not created:
            order.quantity += 1
            order.save()
            
    return redirect('homepage')
    

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
