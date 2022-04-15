from django.urls import path
from . import views

urlpatterns = [
    # path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    # path('api/groups', views.GroupList.as_view(), name='group_list'),
    # path('api/groups/<int:pk>', views.GroupDetail.as_view(), name='group_detail'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout')
]