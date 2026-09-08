from django.urls import path

from .views import comentario_list, detalle_comentario, post_list, detalle_post

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', detalle_post, name='detalle_post'),
    path('comentarios/', comentario_list, name='comentario_list'),
    path('comentarios/<int:pk>/', detalle_comentario, name='detalle_comentario'),
]