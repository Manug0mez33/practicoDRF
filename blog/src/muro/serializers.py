from rest_framework import serializers
from .models import Muro

class MuroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muro
        fields = [
            'id',
            'titulo', 
            'contenido', 
            'timestamp',
            ]

        read_only_fields = [
            'id', 
            'timestamp',
            ]