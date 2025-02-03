from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from .models import Product
from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'BF/home.html') 

def login(request):
    if request.method == 'POST':
        # Handle POST request
        username = request.POST['username']
        password = request.POST['password']
        # Perform authentication here
        # If authentication is successful
        return render(request, 'BF/test.html')
    else:
        # If GET request or any other method
        return render(request, 'BF/login.html')


User = get_user_model()
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
        else:
            return render(request, 'BF/signup.html', {'form': form})  # Re-render the form with errors
    else:
        form = UserCreationForm()

    return render(request, 'BF/signup.html', {'form': form})

#@login_required
def buynow(request):
    products = Product.objects.all()
    return render(request, 'BF/test.html',{'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'BF/product_detail.html', {'product': product})



def product_list(request):
    products = Product.objects.all()
    print("Products fetched from the database:")
    for product in products:
        print(f"Name: {product.name}, Price: {product.price}, Image: {product.image.url}")
    
    # Debug: Check if products are being passed to the template
    print(f"Number of products passed to template: {products.count()}")
    
    return render(request, 'BF/test.html', {'products': products})









