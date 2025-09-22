from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.models.guia import Guia
from backend.models.cliente import Cliente
from backend.models.direccion import Direccion
from backend.models.empresa import Empresa
from backend.models.oficina import Oficina

@receiver(post_save, sender=Guia)
def procesar_guia(sender, instance, created, **kwargs):
    if not created:
        return

    # Crear o recuperar cliente remitente
    Cliente.objects.get_or_create(
        nombres=instance.src_nombres,
        apellido_uno=instance.src_apellido_uno,
        apellido_dos=instance.src_apellido_dos,
        telefono_uno=instance.src_telefono_uno
        telefono_dos=instance.src_telefono_dos
    )

    # Crear o recuperar cliente destinatario
    Cliente.objects.get_or_create(
        nombres=instance.dst_nombres,
        apellido_paterno=instance.dst_apellido_uno,
        apellido_materno=instance.dst_apellido_dos,
        telefono_uno=instance.dst_telefono_uno
        telefono_dos=instance.dst_telefono_dos
    )

    # Crear o recuperar dirección remitente
    Direccion.objects.get_or_create(
        pais=instance.src_pais,
        estado=instance.src_estado,
        ciudad=instance.src_ciudad,
        direccion_uno=instance.src_direccion_uno,
        direccion_dos=instance.src_direccion_dos
    )

    # Crear o recuperar dirección destinatario
    Direccion.objects.get_or_create(
        pais=instance.dst_pais,
        estado=instance.dst_estado,
        ciudad=instance.dst_ciudad,
        direccion_uno=instance.dst_direccion_uno,
        direccion_dos=instance.dst_direccion_dos
    )

    # Crear o recuperar empresa
    Empresa.objects.get_or_create(nombre=instance.empresa)

    # Crear o recuperar agencia
    Oficina.objects.get_or_create(nombre=instance.oficina)
