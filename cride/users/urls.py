from django.urls import path
from django.conf.urls import url

from rest_framework.authtoken import views

from cride.users.views.users import (
    UserLoginAPIView, 
    CustomAuthToken,
    UserSignupAPIView
    )

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignupAPIView.as_view(), name='user_signup'),
    url(r'^api-token-auth/', CustomAuthToken.as_view(), name='custom_token'),
]