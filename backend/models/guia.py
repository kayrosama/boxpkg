from django.db import models
from django.utils import timezone
from backend.constants import STS_PAGO
from backend.models.addresses import State, Country, ZipCode


class Guia(models.Model):
    # Datos del remitente
    src_nombres = models.CharField(max_length=50, blank=True, null=True)
    src_apellidos = models.CharField(max_length=50, blank=True, null=True)
    src_telefono_uno = models.CharField(max_length=20, blank=True, null=True)
    src_telefono_dos = models.CharField(max_length=20, blank=True, null=True)
    
    # Dirección del remitente
    src_pais = models.CharField(max_length=50, blank=True, null=True)
    src_estado = models.CharField(max_length=50, blank=True, null=True)
    src_ciudad = models.CharField(max_length=50, blank=True, null=True)
    src_zipcode = models.CharField(max_length=20, blank=True, null=True)
    src_street_uno = models.CharField(max_length=150, blank=True, null=True)
    src_street_dos = models.CharField(max_length=150, blank=True, null=True)

    # Datos del destinatario
    dst_nombres = models.CharField(max_length=50, blank=True, null=True)
    dst_apellidos = models.CharField(max_length=30, blank=True, null=True)
    dst_telefono_uno = models.CharField(max_length=20, blank=True, null=True)
    dst_telefono_dos = models.CharField(max_length=20, blank=True, null=True)

    # Dirección del destinatario
    dst_pais = models.CharField(max_length=50, blank=True, null=True)
    dst_estado = models.CharField(max_length=50, blank=True, null=True)
    dst_ciudad = models.CharField(max_length=50, blank=True, null=True)
    dst_zipcode = models.CharField(max_length=20, blank=True, null=True)
    dst_street_uno = models.CharField(max_length=150, blank=True, null=True)
    dst_street_dos = models.CharField(max_length=150, blank=True, null=True)

    # Datos del paquete
    fecha_crea = models.DateTimeField(auto_now_add=True)
    fecha_guia = models.DateTimeField(default=timezone.now)
    guia_num = models.CharField(max_length=10, unique=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    lista_contenido = models.TextField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    # Empresa y agencia
    empresa = models.CharField(max_length=100, blank=True, null=True)
    oficina = models.CharField(max_length=100, blank=True, null=True)

    sts_pago = models.IntegerField(choices=STS_PAGO, null=True, blank=False, default=None, help_text="Indica si el monto fue pagado (1), no pagado (0).")

    def __str__(self):
        return f"Guía {self.guia_num}"

    def suggest_address(self, estado, ciudad, zipcode):
        return {
            'estado': list(State.objects.filter(abbr__icontains=estado).values_list('abbr', flat=True)),
            'ciudad': list(Country.objects.filter(name__icontains=ciudad).values_list('name', flat=True)),
            'zipcode': list(ZipCode.objects.filter(code__icontains=zipcode).values_list('code', flat=True)),
        }

    def clean(self):
        errors = {}

        # Validar dirección del remitente
        if not State.objects.filter(abbr=self.src_estado).exists():
            errors['src_estado'] = f"Estado remitente '{self.src_estado}' no válido. Sugerencias: {self.suggest_address(self.src_estado, '', '')['estado']}"
        if not Country.objects.filter(name__iexact=self.src_ciudad, state__abbr=self.src_estado).exists():
            errors['src_ciudad'] = f"Ciudad remitente '{self.src_ciudad}' no válida. Sugerencias: {self.suggest_address('', self.src_ciudad, '')['ciudad']}"
        if not ZipCode.objects.filter(code=self.src_zipcode, state__abbr=self.src_estado, city__iexact=self.src_ciudad).exists():
            errors['src_zipcode'] = f"Zipcode remitente '{self.src_zipcode}' no válido. Sugerencias: {self.suggest_address('', '', self.src_zipcode)['zipcode']}"

        # Validar dirección del destinatario
        if not State.objects.filter(abbr=self.dst_estado).exists():
            errors['dst_estado'] = f"Estado destinatario '{self.dst_estado}' no válido. Sugerencias: {self.suggest_address(self.dst_estado, '', '')['estado']}"
        if not Country.objects.filter(name__iexact=self.dst_ciudad, state__abbr=self.dst_estado).exists():
            errors['dst_ciudad'] = f"Ciudad destinatario '{self.dst_ciudad}' no válida. Sugerencias: {self.suggest_address('', self.dst_ciudad, '')['ciudad']}"
        if not ZipCode.objects.filter(code=self.dst_zipcode, state__abbr=self.dst_estado, city__iexact=self.dst_ciudad).exists():
            errors['dst_zipcode'] = f"Zipcode destinatario '{self.dst_zipcode}' no válido. Sugerencias: {self.suggest_address('', '', self.dst_zipcode)['zipcode']}"

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
        
