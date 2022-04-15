# from django.shortcuts import render # used for templates

# Create your views here.
from django.shortcuts import get_object_or_404 # to get single model instance
from rest_framework import generics, status # import generic API views, status module for http response
from rest_framework.response import Response # import to modify CRUD methods
from rest_framework.exceptions import PermissionDenied # import function for raising error when missing token (403 forbidden)
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
    def get(self, request, group_id):
        """GET /discussions""" # not used in routing chart
        # discussions = Discussion.objects.all().order_by('name')
        # to filter by the current group
        discussions = Discussion.objects.filter(group = group_id)
        serializer = DiscussionSerializer(discussions, many=True)
        # in generics -> method_APIVIEW -> get() -> list():
        # serializer = model_serializer(model_queryset, many=True)
        # return Response(serializer.data)
        return Response(serializer.data)

    def post(self, request, group_id):
        """POST /discussions"""
        # set admin field of new discussion to current-user for update/delete access
        request.data['admin'] = request.user.id
        request.data['group'] = group_id ### todo - does this successfully link current group?
        new_discussion = DiscussionSerializer(data=request.data)
        # new_model_instance = model_serializer(data=request.data)
        # { name: 'discussion 1', description: 'description 1' ... }
        # can also -> new_model_instance = model_serializer(data=request.data[model_name])
        # { model_name: { name: 'discussion 1', description: 'description 1' ... }}

        if new_discussion.is_valid(): # serializer validation
            new_discussion.save()
            # responds with data
            return Response(new_discussion.data, status=status.HTTP_201_CREATED)
            # responds with data under `model_name`` property (can send data of related tables with a dictionary)
            # return Response({ model_name: serializer.data, model_name_2: model2_data }, status=status.HTTP_201_CREATED)

        else: # if validation fails
            return Response(new_discussion.errors, status=status.HTTP_400_BAD_REQUEST) 


class DiscussionDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Discussion.objects.all().order_by('id')
    # serializer_class = DiscussionSerializer
    
    def get(self, request, pk):
        """GET /discussions/<int:pk>"""
        discussion = get_object_or_404(Discussion, pk=pk)

        # check that user is in the group that contains this discussion
        if discussion.group not in request.user.groups:
            # raise like throw in js (cause a PermissionDenied error to occur)
            raise PermissionDenied('Unauthorized action')

        serializer = DiscussionSerializer(discussion)
        # only responds with discussion data
        # return Response(serializer.data)
        # responding with discussion and asociated admin's id, group, as well as posts
        return Response({ 'discussion': serializer.data, 'posts': serializer.data['posts'], 'group': serializer.data['group'], 'admin_id': serializer.data['admin'] })
        # in generics -> method_APIVIEW -> get() -> retrieve():
        # serializer = model_serializer(get_object_or_404(model_queryset, **filter_kwargs))
        # return Response(serializer.data)

    def delete(self, request, pk):
        """DELETE /discussions/<int:pk>"""
        discussion = get_object_or_404(Discussion, pk=pk)
        if request.user.id != discussion.admin:
            raise PermissionDenied('Unauthorized action')
        discussion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # update() for put, partial_update() for patch
    def update(self, request, pk):
        """UPDATE /discussions/<int:pk>"""
        # locate discussion to update - returns object representation of found discussion
        discussion = get_object_or_404(Discussion, pk=pk)

        # check that user making request is admin
        if request.user.id != discussion.admin:
            raise PermissionDenied('Unauthorized action')

        # makes sure admin field is set to current user's id (prevents sending false credentials in request data to change admin) 
        request.data['admin'] = request.user.id
        
        # validate updates with serializer 
        # similar format to combining get and post
        serializer = DiscussionSerializer(discussion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: # if serializer validation fails
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
