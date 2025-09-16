from django.test import TestCase
from core_auth.models import User
from backend.models.empresa import Empresa
from backend.models.direcciones import Direccion
from backend.models.catalogos import CatalogoDireccion

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

