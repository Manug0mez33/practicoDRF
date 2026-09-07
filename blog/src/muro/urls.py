from django.urls import path

from .views import muro_list, detalle_post

urlpatterns = [
    path('', muro_list, name='muro-list'),
    path('<int:pk>/', detalle_post, name='detalle_post'),
]