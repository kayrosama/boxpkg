from rest_framework import viewsets
from backend.models.empresa import Empresa
from .serializers import EmpresaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar el CRUD de empresas.
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
