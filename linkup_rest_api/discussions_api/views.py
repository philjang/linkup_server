# from django.shortcuts import render # used for templates

# Create your views here.
from rest_framework import generics # import generic API views
from rest_framework.response import Response # import to modify CRUD methods
from .serializers import DiscussionSerializer, PostSerializer
from .models import Discussion, Post

# views to connect DiscussionSerializer to Discussion model

# 'generics.ListCreateAPIView' inherited by list function to display all instances of the model, or create a new instance, depending on request url and method
# 'generics.RetrieveUpdateDestroyAPIView' inherited by detail function to update or delete instance of the model in database, depending on request url and method
class DiscussionList(generics.ListCreateAPIView):
    # # initial approach w/o auth or customized relationships
    # # retrieve all objects from db, order by ascending id
    # queryset = Discussion.objects.all().order_by('id')
    # # tell django what serializer to use
    # serializer_class = DiscussionSerializer
    def get(self, request):
        """GET /discussions""" # not used in routing chart
        discussions = Discussion.objects.all().order_by('name')
        serializer = DiscussionSerializer(discussions, many=True)
        return Response(serializer.data)
        # in generics -> method_APIVIEW -> get() -> list():
        # serializer = model_serializer(model_queryset, many=True)
        # return Response(serializer.data)
    def post(self, request):
        """POST /discussions"""
class DiscussionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all().order_by('id')
    serializer_class = DiscussionSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
