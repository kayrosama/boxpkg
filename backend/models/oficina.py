from django.db import models
from backend.models.empresa import Empresa, Direccion

class Oficina(models.Model):
    oficina_codigo = models.CharField(max_length=10, unique=True)
    oficina_nombre = models.CharField(max_length=255)
    oficina_telefono = models.CharField(max_length=20)
    oficina_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    oficina_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.oficina_nombre} ({self.oficina_codigo})"
        
    def clean(self):
        if len(self.oficina_codigo) < 8 or len(self.oficina_codigo) > 10:
            raise ValidationError("El código de oficina debe tener entre 8 y 10 caracteres.")
