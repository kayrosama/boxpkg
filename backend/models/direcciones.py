from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from core_auth.models import User
from backend.constants import STS_REGISTRO, STS_TIPO, STS_DIRECCION
from backend.models.catalogos import CatalogoDireccion
import uuid

def generate_numeric_uuid():
    return str(uuid.uuid4().int)[:15]


class Direccion(models.Model):
    catalogo_direccion = models.ForeignKey(CatalogoDireccion, on_delete=models.PROTECT, null=True, blank=True)
    
    direccion_sts_registro = models.IntegerField(choices=STS_REGISTRO, default=1)
    direccion_sts_tipo = models.IntegerField(choices=STS_TIPO, default=1)
    direccion_sts_direccion = models.IntegerField(choices=STS_DIRECCION, default=1)
    
    direccion_codigo = models.CharField(max_length=15, default=generate_numeric_uuid, editable=False)
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    direccion_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    direccion_empresa = models.ForeignKey('backend.Empresa', on_delete=models.CASCADE, null=True, blank=True)
    
    direccion_street_one = models.CharField(max_length=50, null=True, blank=True)
    direccion_street_two = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.direccion_codigo} - {self.get_direccion_estado_uso_display()}"
    
