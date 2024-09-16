from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from api_v2.views import CustomAuthToken, UserCreateAPIView, CurrentUserView

urlpatterns = [
    # Login Type 1
    path('token', obtain_auth_token, name='api_token_auth'),

    # Login Type 2
    path('login', CustomAuthToken.as_view(), name='custom_api_token_auth'),

    path('register', UserCreateAPIView.as_view(), name='create'),

    path('user', CurrentUserView.as_view(), name='current-user'),

]