from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.apis.direcciones.views import DireccionViewSet

router = DefaultRouter()
router.register(r'direcciones/mantenimiento', DireccionViewSet, basename='direccion')

urlpatterns = [
    path('', include(router.urls)),
]

