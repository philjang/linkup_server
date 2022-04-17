from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Circle
from django.apps import apps
Discussion = apps.get_model('discussions_api.Discussion')
# from ..discussions_api.serializers import DiscussionSerializer

# Django uses serializers.ModelSerializer convert sql to JSON
# serializers used to read/create/update models

class DiscussionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Discussion 
        fields = ('id', 'name', 'description', 'admin', 'circle')
    
class CircleSerializer(serializers.ModelSerializer):
    # users = UserSerializer(many=True, read_only=True)
    # discussions = DiscussionSerializer(many=True, read_only=True)
    discussions = serializers.StringRelatedField(many=True, read_only=True) # nested serializers cannot be serialized to send as JSON
    class Meta:
        model = Circle
        # can also use fields = __all__, but best practice to be explicit
        fields = ('id','name', 'discussions', 'admin')

# defined under CircleSerializer to have access for using as self.posts
class UserSerializer(serializers.ModelSerializer): 
    # this serializer is used for user creation
    # login serializer inherits from this serializer to require certain data for login
    circles = CircleSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'circles', 'username', 'email', 'password') ### do I need password removed?
        # prevents sending password along with data when using views
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 }}
    # method used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.Serializer): # note this is using Serializer, not ModelSerializer (no nested class Meta - used just to check two passwords to each other)
    # require username, email, password, and password confirmation for sign up
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # check that password and confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')
        # check if the two passwords match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # return data if both checks pass
        return data