from django.urls import path
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from .views import UserCreate

urlpatterns = [
    path("", UserCreate.as_view(), name='account-create'),
]