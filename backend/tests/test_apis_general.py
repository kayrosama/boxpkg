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

    def test_list_empresas(self):
        url = reverse('empresa')  # Asegúrate que este nombre esté en tus rutas
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_empresa(self):
        url = reverse('empresa')
        data = {
            "empresa_nombre": "Empresa Test",
            "empresa_codigo": "123456789"
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == 201
        assert Empresa.objects.filter(empresa_nombre="Empresa Test").exists()
