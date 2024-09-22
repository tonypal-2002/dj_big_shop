from django.shortcuts import render

def home(request):
    return render(request, 'frontend/home.html')

def login(request):
    return render(request, 'frontend/auth/login.html')

# Create your views here.
