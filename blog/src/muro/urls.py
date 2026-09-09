from django.urls import path

from .views import PostListCreateAPIView, PostDetailAPIView, ComentarioListCreateAPIView, ComentarioDetailAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('comentarios/', ComentarioListCreateAPIView.as_view(), name='comentario_list'),
    path('comentarios/<int:pk>/', ComentarioDetailAPIView.as_view(), name='comentario_detail'),
]