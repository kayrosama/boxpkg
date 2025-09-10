from rest_framework import serializers
from backend.models.direcciones import Direccion

class DireccionSerializer(serializers.ModelSerializer):
    direccion_estado_uso_display = serializers.SerializerMethodField()
    direccion_tipo_registro_display = serializers.SerializerMethodField()
    direccion_estado_registro_display = serializers.SerializerMethodField()

    class Meta:
        model = Direccion
        fields = [
            'id',
            'direccion_codigo',
            'fecha_registro',
            'fecha_modificacion',
            'direccion_estado_registro',
            'direccion_tipo_registro',
            'direccion_estado_uso',
            'direccion_usuario',
            'direccion_empresa',
            'direccion_pais',
            'direccion_estado',
            'direccion_ciudad',
            'direccion_zipcode',
            'direccion_direccion',
            'direccion_casanum',
            'direccion_estado_uso_display',
            'direccion_tipo_registro_display',
            'direccion_estado_registro_display',
        ]

    def get_direccion_estado_uso_display(self, obj):
        return obj.get_direccion_estado_uso_display()

    def get_direccion_tipo_registro_display(self, obj):
        return obj.get_direccion_tipo_registro_display()

    def get_direccion_estado_registro_display(self, obj):
        return obj.get_direccion_estado_registro_display()
