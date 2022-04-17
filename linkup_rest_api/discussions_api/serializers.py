from rest_framework import serializers
from .models import Discussion, Post
from django.contrib.auth import get_user_model

# Django uses serializers.ModelSerializer convert sql to JSON
# serializers used to read/create/update models

## todo - unable to post using PostSerializer without using owner_name for slug_field, but this prevents access to owner_name on read
class ReadPostSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Post
        # can also use fields = '__all__', but best practice to be explicit
        fields = ('id','content','time_posted','discussion','owner')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # can also use fields = '__all__', but best practice to be explicit
        fields = ('id','content','time_posted','discussion','owner')

# defined under PostSerializer to have access for using as self.posts
class DiscussionSerializer(serializers.ModelSerializer): 
    # posts = PostSerializer(many=True, read_only=True) # allows access to related 1:M model using related_name
    posts = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Discussion # dictates which model will be used
        fields = ('id', 'name', 'description', 'posts', 'admin', 'circle')