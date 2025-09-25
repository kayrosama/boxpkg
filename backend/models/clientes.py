from django.db import models

class Cliente(models.Model):
    nombres = models.CharField(max_length=50, null=True, blank=True)
    apellido_uno = models.CharField(max_length=30, null=True, blank=True)
    apellido_dos = models.CharField(max_length=30, null=True, blank=True)
    telefono_uno = models.CharField(max_length=20, null=True, blank=True)
    telefono_dos = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellido_uno} {self.apellido_dos}"
