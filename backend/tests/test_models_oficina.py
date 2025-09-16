from django.test import TestCase
from core_auth.models import User
from backend.models.catalogos import CatalogoDireccion
from backend.models.direcciones import Direccion
from backend.models.empresa import Empresa
from backend.models.oficina import Oficina

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

