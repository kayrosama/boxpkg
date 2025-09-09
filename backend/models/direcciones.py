from django.db import models
from django.core.exceptions import ValidationError
from core_auth.models import User
from backend.models.empresa import Empresa

class Direccion(models.Model):
    direccion_codigo = models.CharField(max_length=10, unique=True)
    direccion_tipo = models.IntegerField()
    direccion_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    direccion_pais = models.CharField(max_length=20)
    direccion_estado = models.CharField(max_length=5)
    direccion_ciudad = models.CharField(max_length=20)
    direccion_zipecode = models.CharField(max_length=20)
    direccion_direccion = models.CharField(max_length=50)
    direccion_casanum = models.CharField(max_length=30)

    def __str__(self):
        return f"Dirección {self.direccion_codigo} (Tipo {self.direccion_tipo})"

    def clean(self):
        if len(self.direccion_codigo) < 8 or len(self.direccion_codigo) > 10:
            raise ValidationError("El código de dirección debe tener entre 8 y 10 caracteres.")
