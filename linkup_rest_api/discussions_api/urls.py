# urls.py and views.py act as controllers
# having separate controllers for each application (grouped models in this case) allows for modularity for apps to be used in different projects

from django.urls import path
from . import views

urlpatterns = [
    # api/discussions urls will be routed to DiscussionList in views
    path('discussions/', views.DiscussionList.as_view(), name='discussion_list'),
    # api/discussions urls will be routed to DiscussionDetail in views
    path('discussions/<int:pk>/', views.DiscussionDetail.as_view(), name='discussion_detail'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail')
]