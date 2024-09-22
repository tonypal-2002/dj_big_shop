from django.urls import path
from frontend.views import home, login, register

urlpatterns = [
    path('', home),
    #path('/', home, name='home'),
    path('login', login, name='login'),
    path('register', register, name='register'),

]