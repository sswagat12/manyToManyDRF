from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import User, UserAddress
from .serializers import UserSerializer, UserAddressSerializer

# Create your views here.

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UerAddressListCreate(generics.ListCreateAPIView):
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()
