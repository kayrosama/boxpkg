from rest_framework import viewsets
from backend.models.guia import Guia
from .serializers import GuiaSerializer

class GuiaViewSet(viewsets.ModelViewSet):
    queryset = Guia.objects.all()
    serializer_class = GuiaSerializer
