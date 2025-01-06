from django.urls import path
from .views import  UserRegistration, UserLogin

urlpatterns = [
    path('login/', UserLogin, name='login'),
    path('register/', UserRegistration, name='register'),
]