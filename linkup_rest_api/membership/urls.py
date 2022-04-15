from django.urls import path
from . import views

urlpatterns = [
    # api/discussions urls will be routed to DiscussionList in views
    path('api/users', views.UserList.as_view(), name='user_list'),
    # api/discussions urls will be routed to DiscussionDetail in views
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/groups', views.GroupList.as_view(), name='group_list'),
    path('api/groups/<int:pk>', views.GroupDetail.as_view(), name='group_detail')
]