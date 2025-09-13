from rest_framework import viewsets, filters
from backend.models.catalogos import CatalogoDireccion
from .serializers import CatalogoDireccionSerializer

class CatalogoDireccionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para autocompletación de direcciones.
    """
    queryset = CatalogoDireccion.objects.all()
    serializer_class = CatalogoDireccionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'state_id', 'state_name', 'city_base', 'city', 'zipcode']
