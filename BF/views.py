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
from .models import Product , PastOrder
from .forms import UserProfileForm, AddressForm, ProfileForm
from .models import Favorite, CartItem


def home(request):
    return render(request, 'BF/home.html') 

def login(request):
    if request.method == 'POST':
        # Handle POST request
        username = request.POST['username']
        password = request.POST['password']
        # Perform authentication here
        # If authentication is successful
        products = Product.objects.all()
        return render(request, 'BF/test.html',{'products': products})
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

# @login_required
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



@login_required(login_url='/login/')
def favorite_products(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    return render(request, 'favorite.html', {'favorites': favorites})


def save_to_favorites(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        user = request.user
        # Create or get the favorite object
        favorite, created = Favorite.objects.get_or_create(user=user, product=product)
        if created:
            # The favorite was created
            favorite.save()
            # You can add messages or other actions here
        return redirect('favourites')  # Update 'some-view-name' to the appropriate view name
    else:
        return redirect('/login/')

@login_required
def past_orders(request):
    past_orders = request.user.past_orders.all()
    return render(request, 'BF/past_orders.html', {'past_orders': past_orders})

@login_required
def user_profile(request):
    return render(request, 'BF/user_profile.html', {'user': request.user})

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile')
    else:
        user_form = UserProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'BF/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('user_profile')
    else:
        form = AddressForm()

    return render(request, 'BF/add_address.html', {'form': form})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})










