from django.urls import path
from frontend.views import home, auth_login,auth_logout, register, forget_password, about, account, show

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', show, name='show'),  # Product detail page
    #path('/', home, name='home'),
    path('login', auth_login, name='login'),
    path('logout/', auth_logout, name='logout'),
    path('register', register, name='register'),
    path('forget_password', forget_password, name='forget_password'),
    path('account', account, name='account'),
    path('about', about, name='about'),

]