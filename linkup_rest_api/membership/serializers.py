from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Group

# Django uses serializers.ModelSerializer convert sql to JSON
# serializers used to read/create/update models
    
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # can also use fields = __all__, but best practice to be explicit
        fields = ('id','name','admin')

# defined under GroupSerializer to have access for using as self.posts
class UserSerializer(serializers.ModelSerializer): 
    # this serializer is used for user creation
    # login serializer inherits from this serializer to require certain data for login
    groups = GroupSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'group')
        # prevents sending password along with data when using views
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 }}
    # method used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)