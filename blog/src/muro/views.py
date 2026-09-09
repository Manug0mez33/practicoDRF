from rest_framework import generics
from .models import Post, Comentario
from .serializers import PostNestedSerializer, PostPublicSerializer, PostSerializer, ComentarioSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().select_related('comentarios')
    serializer_class = PostNestedSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostSerializer
        return PostNestedSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostPublicSerializer

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostSerializer
        return PostPublicSerializer

class ComentarioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ComentarioDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer