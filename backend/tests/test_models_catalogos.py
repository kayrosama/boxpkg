import pytest
from backend.models.catalogos import CatalogoDireccion

@pytest.mark.django_db
def test_catalogo_direccion_creacion_valida():
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

@pytest.mark.django_db
def test_catalogo_direccion_unicidad():
    CatalogoDireccion.objects.create(
        country="Estados Unidos",
        state_id="CA",
        state_name="Los Angeles",
        city_base="Los Angeles",
        city="Los Angeles",
        zipcode="90004"
    )
    with pytest.raises(Exception):
        CatalogoDireccion.objects.create(
            country="Estados Unidos",
            state_id="CA",
            state_name="Los Angeles",
            city_base="Los Angeles",
            city="Los Angeles",
            zipcode="90004"
        )
