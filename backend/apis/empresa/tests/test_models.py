import pytest
from backend.models.empresa import Empresa
from backend.models.direcciones import Direccion
from core_auth.models import User

@pytest.mark.django_db
def test_creacion_empresa_con_relaciones():
    direccion = Direccion.objects.create(direccion_codigo="D001", direccion_detalle="Zona 10")
    contacto = User.objects.create_user(username="admin", password="admin123")
    
    empresa = Empresa.objects.create(
        empresa_codigo="E001",
        empresa_hombre="BoxPkg",
        empresa_contacto=contacto,
        empresa_telefono="12345678",
        empresa_direccion=direccion
    )

    assert empresa.id is not None
    assert empresa.empresa_hombre == "BoxPkg"
    assert empresa.empresa_contacto == contacto
    assert empresa.empresa_direccion == direccion
