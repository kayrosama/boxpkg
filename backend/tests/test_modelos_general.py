import pytest
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from core_auth.models import User
from backend.models import Empresa, Oficina, Direccion, Contacto, CatalogoDireccion


@pytest.mark.django_db
class EmpresaModelTests(TestCase):
    def setUp(self):
        # Crear usuario de contacto
        self.user = User.objects.create_user(email='testuser@kmkz.io', password='12345')

        # Crear catálogo de dirección
        self.catalogo = CatalogoDireccion.objects.create(
            country='Estados Unidos',
            state_id='CA',
            state_name='Los Angeles',
            city_base='Los Angeles',
            city='Los Angeles',
            zipcode='90004'
        )

        # Crear dirección
        self.direccion = Direccion.objects.create(
            direccion_codigo='123456789012345',
            catalogo_direccion=self.catalogo
        )

    def test_creacion_empresa_valida(self):
        empresa = Empresa.objects.create(
            empresa_codigo='EMP00123',
            empresa_nombre='Mi Empresa S.A.',
            empresa_contacto=self.user,
            empresa_telefono='5555-1234',
            empresa_direccion=self.direccion
        )
        self.assertEqual(empresa.empresa_nombre, 'Mi Empresa S.A.')
        self.assertEqual(empresa.empresa_codigo, 'EMP00123')
        self.assertEqual(empresa.empresa_contacto, self.user)
        self.assertEqual(empresa.empresa_direccion, self.direccion)

    def test_empresa_str(self):
        empresa = Empresa.objects.create(
            empresa_codigo='EMP00123',
            empresa_nombre='Mi Empresa S.A.',
            empresa_contacto=self.user,
            empresa_telefono='5555-1234',
            empresa_direccion=self.direccion
        )
        self.assertEqual(str(empresa), 'Mi Empresa S.A. (EMP00123)')


@pytest.mark.django_db
class DireccionModelTests(TestCase):
    def setUp(self):
        # Crear catálogo de dirección
        self.catalogo = CatalogoDireccion.objects.create(
            country='Estados Unidos',
            state_id='CA',
            state_name='Los Angeles',
            city_base='Los Angeles',
            city='Los Angeles',
            zipcode='90004'
        )

    def test_creacion_direccion_valida(self):
        direccion = Direccion.objects.create(
            direccion_codigo='123456789012345',
            catalogo_direccion=self.catalogo
        )
        self.assertEqual(direccion.direccion_codigo, '123456789012345')
        self.assertEqual(direccion.catalogo_direccion, self.catalogo)

    def test_direccion_str(self):
        direccion = Direccion.objects.create(
            direccion_codigo='123456789012345',
            direccion_sts_tipo=1,  # Asumiendo que 1 corresponde a 'Cliente'
            catalogo_direccion=self.catalogo
        )
        self.assertEqual(str(direccion), '123456789012345 - Cliente')


@pytest.mark.django_db
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


@pytest.mark.django_db
class CatalogoDireccionModelTest:

    def test_creacion_valida(self):
        catalogo = CatalogoDireccion.objects.create(
            country="Estados Unidos",
            state_id="CA",
            state_name="Los Angeles",
            city_base="Los Angeles",
            city="Los Angeles",
            zipcode="90004"
        )
        assert catalogo.pk is not None
        assert str(catalogo) == "Estados Unidos - CA - Los Angeles - Los Angeles - Los Angeles - 90004"

    def test_unicidad_catalogo_direccion(self):
        CatalogoDireccion.objects.create(
            country="Estados Unidos",
            state_id="CA",
            state_name="Los Angeles",
            city_base="Los Angeles",
            city="Los Angeles",
            zipcode="90004"
        )
        with pytest.raises(IntegrityError):
            CatalogoDireccion.objects.create(
                country="Estados Unidos",
                state_id="CA",
                state_name="Los Angeles",
                city_base="Los Angeles",
                city="Los Angeles",
                zipcode="90004"
            )


@pytest.mark.django_db
class OficinaModelTests(TestCase):
    def setUp(self):
        # Crear usuario de contacto
        self.user = User.objects.create_user(email='testuser@kmkz.io', password='12345')

        # Crear catálogo de dirección
        self.catalogo = CatalogoDireccion.objects.create(
            country='Estados Unidos',
            state_id='CA',
            state_name='Los Angeles',
            city_base='Los Angeles',
            city='Los Angeles',
            zipcode='90004'
        )

        # Crear dirección
        self.direccion = Direccion.objects.create(
            direccion_codigo='123456789012345',
            catalogo_direccion=self.catalogo
        )

        # Crear empresa
        self.empresa = Empresa.objects.create(
            empresa_codigo='EMP00123',
            empresa_nombre='Mi Empresa S.A.',
            empresa_contacto=self.user,
            empresa_telefono='5555-1234',
            empresa_direccion=self.direccion
        )

    def test_creacion_oficina_valida(self):
        oficina = Oficina.objects.create(
            oficina_codigo='OFIC001',
            oficina_nombre='Oficina Central',
            oficina_empresa=self.empresa,
            oficina_direccion=self.direccion
        )
        self.assertEqual(oficina.oficina_nombre, 'Oficina Central')
        self.assertEqual(oficina.oficina_codigo, 'OFIC001')
        self.assertEqual(oficina.oficina_empresa, self.empresa)
        self.assertEqual(oficina.oficina_direccion, self.direccion)

    def test_oficina_str(self):
        oficina = Oficina.objects.create(
            oficina_codigo='OFIC001',
            oficina_nombre='Oficina Central',
            oficina_empresa=self.empresa,
            oficina_direccion=self.direccion
        )
        self.assertEqual(str(oficina), 'Oficina Central (OFIC001)')
