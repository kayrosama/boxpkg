from rest_framework import serializers
from backend.models.empresa import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'empresa_codigo',
            'empresa_nombre',
            'empresa_contacto',
            'empresa_telefono',
            'empresa_direccion',
        ]
        read_only_fields = ['empresa_codigo']
