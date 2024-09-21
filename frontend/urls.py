from django.urls import path
from frontend.views import  home,

urlpatterns = [
    path('', home),
    path('/', home, name='home'),

]