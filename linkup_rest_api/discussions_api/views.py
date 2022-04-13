from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import DiscussionSerializer
from .models import Discussion

# views to connect DiscussionSerializer to Discussion model

# 'generics.ListCreateAPIView' inherited by list function to display all instances of the model, or create a new instance, depending on request url and method
# 'generics.RetrieveUpdateDestroyAPIView' inherited by detail function to update or delete instance of the model in database, depending on request url and method
class DiscussionList(generics.ListCreateAPIView):
    # retrieve all objects from db, order by ascending id
    queryset = Discussion.objects.all().order_by('id')
    # tell django what serializer to use
    serializer_class = DiscussionSerializer

class DiscussionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all().order_by('id')
    serializer_class = DiscussionSerializer