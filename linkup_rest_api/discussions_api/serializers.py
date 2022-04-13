from rest_framework import serializers
from .models import Discussion

# Django uses serializers.ModelSerializer convert sql to JSON
class DiscussionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Discussion # dictates which model will be used
        fields = ('id', 'name', 'description', 'admin', 'group')