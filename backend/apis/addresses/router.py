from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StateViewSet, CountryViewSet, ZipCodeViewSet, autocomplete_address

router = DefaultRouter()
router.register(r'states', StateViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'zipcodes', ZipCodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('autocomplete-address/', autocomplete_address, name='autocomplete-address'),
]
