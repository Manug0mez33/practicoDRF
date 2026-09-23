from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from muro.permissions import GroupEditPermission
from .models import Post, Comentario
from .serializers import PostNestedSerializer, PostPublicSerializer, PostSerializer, ComentarioSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('comentarios')
    permission_classes = [GroupEditPermission]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostNestedSerializer
        return PostSerializer

    @action(detail=True, methods=["post"])
    def borrado_logico(self, request, pk=None):
        post = self.get_object()
        post.activo = False
        post.save()
        return Response({"status": "Post eliminado."})

class ComentarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


# class PostListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.all().select_related('comentarios')
#     permission_classes = [GroupEditPermission]

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return PostSerializer
#         return PostNestedSerializer

# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostPublicSerializer

#     def get_serializer_class(self):
#         if self.request.method in ['PUT', 'PATCH']:
#             return PostSerializer
#         return PostPublicSerializer

# class ComentarioListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer

# class ComentarioDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer