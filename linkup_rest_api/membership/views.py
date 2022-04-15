from webbrowser import get
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework import generics, status
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .serializers import GroupSerializer, UserRegisterSerializer, UserSerializer
from .models import Group


# Create your views here.
class Register(generics.CreateAPIView):
    # override default authentication/permissions classes for this endpoint
    authentication_classes = ()
    permission_classes = ()

    # serializer classes required for endpoints that create data
    serializer_class = UserRegisterSerializer

    def post(self, request):
        """POST /register"""
        # passes request data to validate, doesn't create a model instance (not using Modelserializer)
        user = UserRegisterSerializer(data=request.data)
        if user.is_valid(): # passes RegisterSerializer checks for password
            # actually create the User instance using UserSerializer's create method
            created_user = UserSerializer(data=user.data)
            if created_user.is_valid(): 
                # save the user to db if it passes serializer validation
                created_user.save()
                return Response(created_user.data, status=status.HTTP_201_CREATED)
            else: # UserSerializer validation failed
                return Response(created_user.errors, status=status.HTTP_400_BAD_REQUEST)
        else: # UserRegisterSerializer validation failed
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

class LogIn(generics.CreateAPIView):
    pass
       
class LogOut(generics.DestroyAPIView):
    pass

class UserDetail(generics.ListAPIView):
    pass

class GroupList(generics.ListCreateAPIView):
    # permission_classes=(IsAuthenticated)
    def get(self, request):
        """GET /groups"""
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)
        # # might be needed later, but not in routing chart

    # serializer_class used when posting group
    serializer_class = GroupSerializer
    def post(self, request):
        """POST /groups"""
        request.data['admin'] = request.user.id
        new_group = GroupSerializer(data=request.data)
        if new_group.is_valid():
            new_group.save()
            return Response(new_group.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_group.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=(IsAuthenticated)
        # set by default in settings.py
        # if we only want to show a discussion if the user is signed in
        # like requiresToken middleware from express projects
    def get(self, request, pk):
        """GET /groups/<int:pk>"""
        group = get_object_or_404(Group, pk=pk)
        if request.user not in group.users:
            raise PermissionDenied('Unauthorized action')
        serializer = GroupSerializer(group)
        return Response({ 'group': serializer.data, 'users': serializer.data['users'], 'discussions': serializer.data['discussions'], 'admin_id': serializer.data['admin'] })

    def delete(self, request, pk):
        """DELETE /groups/<int:pk>"""
        group = get_object_or_404(Group, pk=pk)
        if group.admin != request.user.id:
            raise PermissionDenied('Unauthorized action')
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        """UPDATE /groups/<int:pk>"""
        group = get_object_or_404(Group, pk=pk)
        if request.user.id != group.admin:
            raise PermissionDenied('Unauthorized action')
        request.data['admin'] = request.user.id
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
