from django.shortcuts import render


from rest_framework import generics
from .serializers import *

class AdminRegistrationView(generics.CreateAPIView):
    serializer_class = AdminRegistrationSerializer

