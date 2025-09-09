from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatalogoDireccionViewSet

router = DefaultRouter()
router.register(r'direcciones', CatalogoDireccionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
