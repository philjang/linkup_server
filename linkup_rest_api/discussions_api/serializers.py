from rest_framework import serializers
from .models import Discussion, Post

# Django uses serializers.ModelSerializer convert sql to JSON
# serializers used to read/create/update models
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # can also use fields = '__all__', but best practice to be explicit
        fields = ('id','content','time_posted','discussion','owner')

# defined under PostSerializer to have access for using as self.posts
class DiscussionSerializer(serializers.ModelSerializer): 
    # posts = PostSerializer(many=True, read_only=True) # allows access to related 1:M model using related_name
    posts = serializers.StringRelatedField(many=True)
    class Meta:
        model = Discussion # dictates which model will be used
        fields = ('id', 'name', 'description', 'posts', 'admin', 'circle')