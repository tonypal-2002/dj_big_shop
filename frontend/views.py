from django.shortcuts import render

def home(request):
    return render(request, 'frontend/home.html')

def forget_password(request):
    return render(request, 'frontend/forget_password.html')
# Create your views here.
