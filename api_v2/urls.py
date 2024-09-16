from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from api_v2.views import CustomAuthToken, UserCreateAPIView, CurrentUserView, LogoutAPIView, CategoryListView, \
    BrandListView, ProductListView

urlpatterns = [
    # Login Type 1
    path('token', obtain_auth_token, name='api_token_auth'),

    # Login Type 2
    path('login', CustomAuthToken.as_view(), name='custom_api_token_auth'),

    path('register', UserCreateAPIView.as_view(), name='create'),

    path('user', CurrentUserView.as_view(), name='current-user'),

    # Logout
    path('logout', LogoutAPIView.as_view(), name='logout'),

    # Category
    path('categories', CategoryListView.as_view(), name='category_list'),

    # Brand
    path('brands', BrandListView.as_view(), name='brand_list'),

    # Product
    path('products', ProductListView.as_view(), name='product_list'),
]