from django.urls import path, include
from rest_framework.routers import DefaultRouter
from muro import views

router = DefaultRouter()

router.register("posts", views.PostViewSet, basename="posts")
router.register("comentarios", views.ComentarioViewSet, basename="comentarios")