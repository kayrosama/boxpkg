from django.db import models
from core_auth.models import User
from backend.models.direcciones import Direccion


class Empresa(models.Model):
    empresa_codigo = models.CharField(max_length=10, unique=True)
    empresa_nombre = models.CharField(max_length=255)
    empresa_contacto = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa_telefono = models.CharField(max_length=20)
    empresa_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.empresa_nombre} ({self.empresa_codigo})"

    def clean(self):
        if len(self.empresa_codigo) < 8 or len(self.empresa_codigo) > 10:
            raise ValidationError("El código de empresa debe tener entre 8 y 10 caracteres.")
