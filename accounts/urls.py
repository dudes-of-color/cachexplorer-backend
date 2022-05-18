from django.urls import path
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from .views import UserCreate, UserLogout

urlpatterns = [
    path("register/", UserCreate.as_view(), name='account-create'),
    path("logout/", UserLogout.as_view(), name='user-logout')
]