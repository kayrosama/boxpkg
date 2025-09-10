from django.db import models
from django.core.exceptions import ValidationError
from core_auth.models import User


class Direccion(models.Model):
    direccion_codigo = models.CharField(max_length=10, unique=True)
    
    # Auditoría
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    # Logica para registro de registo
    SELECT_REGISTRO = [
        (0, 'Inactivo'),
        (1, 'Activo'),
    ]
    direccion_estado_registro = models.IntegerField(choices=SELECT_REGISTRO, default=1)
    
    # Logica para tipo de registo
    SELECT_TIPO = [
        (0, 'Inactivo'),
        (1, 'Cliente'),
        (2, 'Usuario'),
        (3, 'Proveedor'),
        (4, 'Inmueble'),
    ]
    direccion_tipo_registro = models.IntegerField(choices=SELECT_TIPO, default=1)
    
    # Logica para estado de la dirección
    SELECT_ESTADO = [
        (0, 'Inactivo'),
        (1, 'Principal'),
        (2, 'Secundaria'),
    ]
    direccion_estado_uso = models.IntegerField(choices=SELECT_ESTADO, default=1)
    
    direccion_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    direccion_empresa = models.ForeignKey('backend.Empresa', on_delete=models.CASCADE, null=True, blank=True)
    
    # Logica para country de la direccion
    SELECT_COUNTRY = [
        ('USA', 'Estado Unidos'),
        ('GUA', 'Guatemala'),
    ]
    direccion_country = models.CharField(max_length=20, choices=SELECT_COUNTRY, default='Estados Unidos')

    # Logica para state de la direccion
    SELECT_STATE = [
        ('CA', 'California'),
        ('GUA', 'Guatemala'),
    ]
    direccion_state = models.CharField(max_length=5, choices=SELECT_STATE, default='CA')

    # Logica para city de la direccion
    SELECT_CITY = [
        ('LAX', 'Los Angeles'),
        ('SFO', 'San Francisco'),
        ('GUA', 'Guatemala'),
    ]
    direccion_city = models.CharField(max_length=20, choices=SELECT_CITY, default='Los Angeles')
    
    # Logica para zipcode de la direccion
    SELECT_ZIP = [
        ('900', '90004'),
        ('010', '01011'),
    ]
    direccion_zipcode = models.CharField(max_length=20, choices=SELECT_ZIP, default='90004')
    direccion_street = models.CharField(max_length=50, null=True, blank=True)
    direccion_ = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return f"{self.direccion_codigo} - {self.get_direccion_estado_uso_display()}"

    def clean(self):
        if not (8 <= len(self.direccion_codigo) <= 10):
            raise ValidationError("El código de dirección debe tener entre 8 y 10 caracteres.")

