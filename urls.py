
from django.urls import path
from .views import UserAPIView, UserDetailAPIView, PostAPIView, PostDetailAPIView, LikeAPIView, LikeDetailAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('posts/', PostAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('likes/', LikeAPIView.as_view(), name='like-list'),
    path('likes/<int:pk>/', LikeDetailAPIView.as_view(), name='like-detail'),
]
