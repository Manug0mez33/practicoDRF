from rest_framework import serializers
from .models import Post, Comentario


class PostPublicSerializer(serializers.ModelSerializer):
    comentarios = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'titulo', 
            'contenido',
            'comentarios',
            ]

        read_only_fields = [
            'id', 
            'timestamp',
            ]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'titulo', 
            'contenido',
            'comentarios',
            'timestamp',
            ]

        read_only_fields = [
            'id', 
            'timestamp',
            ]

        nullable_fields = [
            'comentarios',
        ]

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = [
            'id',
            'contenido',
            'timestamp',
        ]
        read_only_fields = [
            'id',
            'timestamp',
        ]

class PostNestedSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'titulo', 
            'contenido',
            'comentarios',
            'timestamp',
            'activo',
        ]
        read_only_fields = [
            'id',
            'timestamp',
            'activo',
        ]
