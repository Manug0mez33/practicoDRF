from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Muro
from .serializers import MuroSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def muro_list(request):
    if request.method == 'GET':
        muros = Muro.objects.all()
        serializer = MuroSerializer(muros, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MuroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_post(request, pk):
    muro = get_object_or_404(Muro, pk=pk)
    if request.method == 'GET':
        serializer = MuroSerializer(muro)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MuroSerializer(muro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        muro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)