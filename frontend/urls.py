from django.urls import path
from frontend.views import home, login, register, forget_password, about

urlpatterns = [
    path('', home),
    #path('/', home, name='home'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('forget_password', forget_password, name='forget_password'),
    path('about', about, name='about'),

]