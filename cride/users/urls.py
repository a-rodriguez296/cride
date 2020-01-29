from django.urls import path
from django.conf.urls import url

from rest_framework.authtoken import views

from cride.users.views.users import UserLoginAPIView, CustomAuthToken

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    url(r'^api-token-auth/', CustomAuthToken.as_view(), name='custom_token'),
]