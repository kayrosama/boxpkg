import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from core_auth.models import User
from backend.models.empresa import Empresa
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
class TestEmpresaAPI:

    def setup_method(self):
        self.user = User.objects.create_user(email='master@kmkz.io', password='Kinteki.')
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
    
        # Crear dirección requerida para el test
        self.direccion = Direccion.objects.create(
            calle="Calle Ficticia",
            ciudad="Ciudad Test",
            pais="GT"
        )
    
    def test_list_empresas(self):
        url = reverse('empresa-list')  # Asegúrate que este nombre esté en tus rutas
        response = self.client.get(url)
        assert response.status_code == 200
    
    def test_create_empresa(self):
        url = reverse('empresa-list')
        data = {
            "empresa_nombre": "Empresa Test",
            "empresa_codigo": "12345678",  # entre 8 y 10 caracteres
            "empresa_contacto": self.user.id,
            "empresa_telefono": "555-1234",
            "empresa_direccion": self.direccion.id
        }
        response = self.client.post(url, data, format='json')
        print(response.data)  # útil si falla
        assert response.status_code == 201
        assert Empresa.objects.filter(empresa_nombre="Empresa Test").exists()
    
