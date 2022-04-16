from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('groups/', views.CircleList.as_view(), name='group_list'),
    path('groups/<int:pk>/', views.CircleDetail.as_view(), name='group_detail')
]