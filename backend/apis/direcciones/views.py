from rest_framework import viewsets
from backend.models.direcciones import Direccion
from .serializers import DireccionSerializer
from rest_framework.permissions import IsAuthenticated

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [IsAuthenticated]
