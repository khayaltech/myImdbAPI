from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import logoutView, registirationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
  #For Both of them
  path('register/',registirationView,name='register'),

  #For Token Authentication
  path('login/',obtain_auth_token,name='login'),
  path('logout/',logoutView,name='logout'),
  
  #For JWT authentication
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
