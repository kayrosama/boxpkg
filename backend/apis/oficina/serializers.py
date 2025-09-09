from rest_framework import serializers
from backend.models.oficina import Oficina

class OficinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oficina
        fields = [
            'oficina_codigo',
            'oficina_nombre',
            'oficina_telefono',
            'oficina_empresa',
            'oficina_direccion',
        ]
        read_only_fields = ['oficina_codigo']
