from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StateViewSet, CountryViewSet, ZipCodeViewSet, autocomplete_address

router = DefaultRouter()
router.register(r'addresses/states', StateViewSet)
router.register(r'addresses/countries', CountryViewSet)
router.register(r'addresses/zipcodes', ZipCodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('addresses/autocomplete-address/', autocomplete_address, name='autocomplete-address'),
]
