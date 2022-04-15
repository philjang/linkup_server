from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class Register(generics.CreateAPIView):
    pass

class LogIn(generics.CreateAPIView):
    pass

class LogOut(generics.DestroyAPIView):
    pass

class UserDetail(generics.ListAPIView):
    pass

class GroupList(generics.ListCreateAPIView):
    pass

    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/groups', views.GroupList.as_view(), name='group_list'),
    path('api/groups/<int:pk>', views.GroupDetail.as_view(), name='group_detail'),