from django.shortcuts import render

def home(request):
    return render(request, 'frontend/home.html')

def login(request):
    return render(request, 'frontend/auth/login.html')

def register(request):
    return render(request, 'frontend/auth/register.html')

def forget_password(request):
    return render(request, 'frontend/auth/forget_password.html')

def about(request):
    return render(request, 'frontend/auth/about.html')

# Create your views here.
