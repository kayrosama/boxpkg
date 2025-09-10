from rest_framework import serializers
from backend.apis.catalogos.serializers import CatalogoDireccionSerializer
from backend.models.direcciones import Direccion

class DireccionSerializer(serializers.ModelSerializer):
    catalogo_direccion = CatalogoDireccionSerializer()

    class Meta:
        model = Direccion
        fields = [
            'direccion_codigo',
            'fecha_registro',
            'fecha_modificacion',
            'direccion_usuario',
            'direccion_empresa',
            'direccion_sts_direccion',
            'direccion_street_one',
            'direccion_street_two',
            'catalogo_direccion',
        ]
        read_only_fields = ['direccion_codigo', 'fecha_registro', 'fecha_modificacion']
