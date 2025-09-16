from django.test import TestCase
from django.core.exceptions import ValidationError
from backend.models.contactos import Contacto
from backend.models.catalogos import CatalogoDireccion
from backend.models.direcciones import Direccion


class ContactoModelTests(TestCase):
    def setUp(self):
        self.catalogo = CatalogoDireccion.objects.create(
            country='Estados Unidos',
            state_id='CA',
            state_name='Los Angeles',
            city_base='Los Angeles',
            city='Los Angeles',
            zipcode='90004'
        )
        self.direccion = Direccion.objects.create(
            direccion_codigo='123456789012345',
            catalogo_direccion=self.catalogo
        )

    def test_creacion_contacto_valido(self):
        contacto = Contacto.objects.create(
            contacto_tipo=1,
            contacto_cui_tipo=1,
            contacto_cui_registro='1234567890101',
            contacto_nombres='Juan',
            contacto_apellido_uno='Pérez',
            contacto_apellido_dos='Gómez',
            contacto_telefono='5555-1234',
            contacto_correo='juan.perez@example.com',
            contacto_direccion=self.direccion
        )
        self.assertEqual(contacto.contacto_nombres, 'Juan')
        self.assertEqual(contacto.contacto_correo, 'juan.perez@example.com')
        self.assertEqual(contacto.contacto_telefono, '5555-1234')

    def test_contacto_str(self):
        contacto = Contacto.objects.create(
            contacto_tipo=1,
            contacto_cui_tipo=1,
            contacto_cui_registro='1234567890101',
            contacto_nombres='Ana',
            contacto_apellido_uno='Gómez',
            contacto_apellido_dos='López',
            contacto_telefono='5555-5678',
            contacto_correo='ana.gomez@example.com',
            contacto_direccion=self.direccion
        )
        self.assertEqual(str(contacto), 'Ana (1)')
        
    def test_codigo_valido_en_clean(self):
        contacto = Contacto(
            contacto_codigo='12345678',
            contacto_tipo=1,
            contacto_cui_tipo=1,
            contacto_nombres='Luis',
            contacto_apellido_uno='Mendez',
            contacto_apellido_dos='Lopez',
            contacto_telefono='5555-0000',
            contacto_correo='luis@example.com',
            contacto_direccion=self.direccion
        )
        try:
            contacto.clean()  # No debe lanzar excepción
        except ValidationError:
            self.fail("clean() lanzó ValidationError con código válido")

    def test_codigo_muy_corto_en_clean(self):
        contacto = Contacto(
            contacto_codigo='1234567',  # 7 caracteres
            contacto_tipo=1,
            contacto_cui_tipo=1,
            contacto_nombres='Luis',
            contacto_apellido_uno='Mendez',
            contacto_apellido_dos='Lopez',
            contacto_telefono='5555-0000',
            contacto_correo='luis@example.com',
            contacto_direccion=self.direccion
        )
        with self.assertRaises(ValidationError):
            contacto.clean()

    def test_codigo_muy_largo_en_clean(self):
        contacto = Contacto(
            contacto_codigo='1234567890123456',  # 16 caracteres
            contacto_tipo=1,
            contacto_cui_tipo=1,
            contacto_nombres='Luis',
            contacto_apellido_uno='Mendez',
            contacto_apellido_dos='Lopez',
            contacto_telefono='5555-0000',
            contacto_correo='luis@example.com',
            contacto_direccion=self.direccion
        )
        with self.assertRaises(ValidationError):
            contacto.clean()
