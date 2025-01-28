from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm



def home(request):
    return render(request, 'BF/home.html') 

def login(request):
    if request.method == 'POST':
        # Handle POST request
        username = request.POST['username']
        password = request.POST['password']
        # Perform authentication here
        # If authentication is successful
        return render(request, 'BF/buynow.html')
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
            return render(request, 'signup.html', {'form': form})  # Re-render the form with errors
    else:
        form = UserCreationForm()

    return render(request, 'BF/signup.html', {'form': form})

@login_required
def buynow(request):
    return render(request, 'BF/test.html')





