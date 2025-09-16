from django.test import TestCase
from backend.models.catalogos import CatalogoDireccion
from backend.models.direcciones import Direccion

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
