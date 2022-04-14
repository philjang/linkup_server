from rest_framework import serializers
from .models import Discussion, Post

# Django uses serializers.ModelSerializer convert sql to JSON
class DiscussionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Discussion # dictates which model will be used
        fields = ('id', 'name', 'description', 'admin', 'group')
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','content','time_posted','discussion','user')