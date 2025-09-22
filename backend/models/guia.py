from django.db import models
from django.utils import timezone
from backend.constants import DIR_COUNTRY, DIR_STATE, DIR_CITY, STS_PAGO


class Guia(models.Model):
    # Datos del remitente
    src_nombres = models.CharField(max_length=50, blank=True, null=True)
    src_apellido_uno = models.CharField(max_length=30, blank=True, null=True)
    src_apellido_dos = models.CharField(max_length=30, blank=True, null=True)
    src_telefono_uno = models.CharField(max_length=20, blank=True, null=True)
    src_telefono_dos = models.CharField(max_length=20, blank=True, null=True)

    # Dirección del remitente
    src_pais = models.CharField(choices=DIR_COUNTRY, default=1)
    src_estado = models.CharField(choices=DIR_STATE, default=1)
    src_ciudad = models.CharField(choices=DIR_CITY, default=1)
    src_zipcode = models.CharField(max_length=20, default=90004)
    src_direccion_uno = models.CharField(max_length=150, blank=True, null=True)
    src_direccion_dos = models.CharField(max_length=150, blank=True, null=True)

    # Datos del destinatario
    dst_nombres = models.CharField(max_length=50, blank=True, null=True)
    dst_apellido_uno = models.CharField(max_length=30, blank=True, null=True)
    dst_apellido_dos = models.CharField(max_length=30, blank=True, null=True)
    dst_telefono_uno = models.CharField(max_length=20, blank=True, null=True)
    dst_telefono_dos = models.CharField(max_length=20, blank=True, null=True)

    # Dirección del destinatario
    dst_pais = models.CharField(choices=DIR_COUNTRY, default=1)
    dst_estado = models.CharField(choices=DIR_STATE, default=1)
    dst_ciudad = models.CharField(choices=DIR_CITY, default=1)
    dst_zipcode = models.CharField(max_length=20, default=90004)
    dst_direccion_uno = models.CharField(max_length=150, blank=True, null=True)
    dst_direccion_dos = models.CharField(max_length=150, blank=True, null=True)

    # Datos del paquete
    guia_num = models.CharField(max_length=10, unique=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion_contenido = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    # Empresa y agencia
    empresa = models.CharField(max_length=100, blank=True, null=True)
    oficina = models.CharField(max_length=100, blank=True, null=True)

    sts_pago = models.IntegerField(choices=STS_PAGO, null=True, blank=False, default=None, help_text="Indica si el monto fue pagado (1), no pagado (0).")

    def __str__(self):
        return f"Guía {self.guia_num}"
