from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class Register(generics.CreateAPIView):
    pass

class LogIn(generics.CreateAPIView):
    pass

class LogOut(generics.DestroyAPIView):
    pass