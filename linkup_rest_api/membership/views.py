from re import M
from webbrowser import get
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework import generics, status
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .serializers import CircleSerializer, UserRegisterSerializer, UserSerializer
from .models import Circle, user_circle


# Create your views here.
class Register(generics.CreateAPIView):
    # override default authentication/permissions classes for this endpoint
    authentication_classes = ()
    permission_classes = ()

    # serializer classes required for endpoints that create data
    serializer_class = UserRegisterSerializer

    def post(self, request):
        """POST membership/register/"""
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
    authentication_classes = ()
    permission_classes = ()

    serializer_class = UserSerializer

    def post(self, request):
        """POST membership/login/"""
        credentials = request.data
        # pass username and password along with request to django's authenticate method
        user = authenticate(request, username=credentials['username'], password=credentials['password'])
        # authentication conditionals
        if user is not None:
            if user.is_active:
                login(request, user)
                # return response with token
                return Response({ 'id': user.id, 'username': user.username, 'token': user.get_auth_token() })
                # return Response({ 'user': { 'id': user.id, 'username': user.username, 'token': user.get_auth_token() }})
            else: # failed active status validation
                return Response({ 'msg': 'The account is inactive.'}, status=status.HTTP_400_BAD_REQUEST)
        else: # failed django authenticate method
            return Response({ 'msg': 'The username and/or password is incorrect.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
 

class LogOut(generics.DestroyAPIView):
    def delete(self, request):
        """DELETE membership/logout/"""
        # remove token from user
        request.user.delete_token()
        # django logout method removes all session data
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetail(generics.RetrieveAPIView):
    def get(self, request, pk):
        """GET membership/users/<int:pk>/"""
        if request.user.id != pk:
            raise PermissionDenied('Unauthorized action')
        user = request.user
        # print(user)
        serializer = UserSerializer(user)
        # print(serializer)
        return Response({ 'user': serializer.data, 'circles': serializer.data['circles'] })


class CircleList(generics.ListCreateAPIView):
    # permission_classes=(IsAuthenticated)
    def get(self, request):
        """GET membership/groups/""" # not used in routing chart
        circles = Circle.objects.all()
        serializer = CircleSerializer(circles, many=True)
        return Response(serializer.data)
        # # might be needed later, but not in routing chart for now

    # serializer_class used when posting group
    serializer_class = CircleSerializer
    def post(self, request):
        """POST membership/groups/"""
        request.data['admin'] = request.user.id
        new_circle = CircleSerializer(data=request.data)
        if new_circle.is_valid():
            new_circle.save()
            # print(new_circle)
            circle = get_object_or_404(Circle, pk=new_circle.data['id']) # retrieve created circle, unsure how to make this cleaner (unsure how to access created instance when using serializers)
            # print(circle)
            circle.users.add(request.user)
            circle.save()
            return Response(new_circle.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_circle.errors, status=status.HTTP_400_BAD_REQUEST)


class CircleDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes=(IsAuthenticated)
        # set by default in settings.py
        # if we only want to show a discussion if the user is signed in
        # like requiresToken middleware from express projects
    def get(self, request, pk):
        """GET membership/groups/<int:pk>/"""
        circle = get_object_or_404(Circle, pk=pk)
        # print(request.user)
        # print(circle.users.all())
        if request.user not in circle.users.all():
            raise PermissionDenied('Unauthorized action')
        serializer = CircleSerializer(circle)
        # print(f'serializer: {serializer.data}')
        # Circle.objects.filter(discussions__circle=circle) # to filter many from 1 
        # todo -- how to display users associated to circle
        users = circle.users.all()
        user_serializer = []
        for user in users:
            user_serializer.append(UserSerializer(user).data)
        return Response({ 'circle': serializer.data, 'users': user_serializer, 'discussions': serializer.data['discussions'], 'admin_id': serializer.data['admin'] })

    def delete(self, request, pk):
        """DELETE membership/groups/<int:pk>/"""
        circle = get_object_or_404(Circle, pk=pk)
        if request.user.id != circle.admin:
            raise PermissionDenied('Unauthorized action')
        circle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk):
        """UPDATE membership/groups/<int:pk>/"""
        circle = get_object_or_404(Circle, pk=pk)
        if request.user.id != circle.admin:
            raise PermissionDenied('Unauthorized action')
        request.data['admin'] = request.user.id
        serializer = CircleSerializer(circle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# add view to allow adding other users to circle
