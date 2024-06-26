from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import FruitInventoryForm
from .models import FruitInventory, UserCart

# Create your views here.
def homepage(request):
    fruits = FruitInventory.objects.all()
    if request.session.has_key('profile_user'):
        user = request.session['profile_user']
        usercart = UserCart.objects.filter(email=request.session['profile.email'])
        totalOrders = usercart.count()
        finalCart = []
        cartTotal = 0
        for item in usercart:
            finalCartItem = {'name': item.item_name}
            for fruit in fruits:
                if item.item_name == fruit.item_name:
                    finalCartItem['quantity'] = item.quantity
                    finalCartItem['price'] = fruit.item_price
                    finalCartItem['total'] = item.quantity * fruit.item_price
                    finalCart.append(finalCartItem)
                    cartTotal += finalCartItem['total']
        print(finalCart)
    else:
        finalCart = totalOrders = cartTotal = user = None
    return render(request, 'homebase.html',
                  {'fruits': fruits,
                   'username': user,
                   'cart': finalCart,
                   'totalOrders': totalOrders,
                   'cartTotal': cartTotal,
                   }
                  )

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

def remove_from_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('parameter')
        print(item_name)
        order = UserCart.objects.get(
            email=request.session['profile.email'],
            item_name=item_name,
            )
        if order.quantity == 1:
            order.delete()
        else:
            order.quantity -= 1
            order.save()
    return redirect('homepage')
    

def profile_settings(request):
    if request.session.has_key('profile_user'):
        user = request.session['profile_user']
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
