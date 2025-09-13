import pytest
from backend.models import Direccion, CatalogoDireccion

@pytest.mark.django_db
def test_creacion_empresa_con_relaciones():
    catalogo = CatalogoDireccion.objects.create(
        country="Estados Unidos",
        state_name="California",
        city="Los Angeles",
        zipcode="90004"
    )
    direccion = Direccion.objects.create(
        direccion_codigo="13000000000001",
        direccion_street_one="4330 Beverly Boulevard",
        catalogo_direccion=catalogo
    )
    assert direccion.pk is not None

