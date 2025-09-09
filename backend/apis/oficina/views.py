from rest_framework import viewsets
from backend.models.oficina import Oficina
from .serializers import OficinaSerializer

class OficinaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar el CRUD de oficinas.
    """
    queryset = Oficina.objects.all()
    serializer_class = OficinaSerializer
