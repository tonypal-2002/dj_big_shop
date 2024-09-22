from django.urls import path
from frontend.views import home, login

urlpatterns = [
    path('', home),
    #path('/', home, name='home'),
    path('login', login, name='login'),

]