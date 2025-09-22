from django.db import models

class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellido_uno = models.CharField(max_length=30)
    apellido_dos = models.CharField(max_length=30)
    telefono_uno = models.CharField(max_length=20)
    telefono_dos = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombres} {self.apellido_uno} {self.apellido_dos}"
