from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from .views import LoginAPIView, RegisterAPIView, AuthAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('auth/', AuthAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
