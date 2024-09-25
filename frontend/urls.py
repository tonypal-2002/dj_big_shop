from django.urls import path
from frontend.views import home, login, register, forget_password, about, account, show

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', show, name='show'),  # Product detail page
    #path('/', home, name='home'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('forget_password', forget_password, name='forget_password'),
    path('account', account, name='account'),
    path('about', about, name='about'),

]