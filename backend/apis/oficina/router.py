from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OficinaViewSet

router = DefaultRouter()
router.register(r'oficinas', OficinaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
