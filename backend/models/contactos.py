from django.db import models
from backend.models.direcciones import Direccion
from backend.constants import TIPO_CONTACTO, CUI_TIPO
import uuid

def generate_numeric_uuid():
    return str(uuid.uuid4(

class Contacto(models.Model):
    contacto_codigo = models.CharField(max_length=15, default=generate_numeric_uuid, editable=False)
    contacto_tipo = models.IntegerField(choices=TIPO_CONTACTO, default=1)
    contacto_cui_tipo = models.IntegerField(choices=CUI_TIPO, default=1)
    contacto_cui_registro = models.CharField(max_length=20, null=True, blank=True)
	contacto_nombres = models.CharField(max_length=100)
	contacto_apellido_uno = models.CharField(max_length=30)
	contacto_apellido_dos = models.CharField(max_length=30)
    contacto_telefono = models.CharField(max_length=20, blank=True, default='')
    contacto_correo = models.EmailField(blank=True, default='')
    contacto_direccion = models.ForeignKey('backend.Direccion', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.contacto_nombres} ({self.contacto_tipo})"
    
    def clean(self):
        if len(self.contacto_codigo) < 8 or len(self.contacto_codigo) > 15:
            raise ValidationError("El código de empresa debe tener entre 8 y 15 caracteres.")
            
