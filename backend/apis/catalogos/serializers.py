from rest_framework import serializers
from backend.models.catalogos import CatalogoDireccion

class CatalogoDireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoDireccion
        fields = [
            'country',
            'state_id',
            'state_name',
            'city_base',
            'city',
            'zipcode',
        ]
