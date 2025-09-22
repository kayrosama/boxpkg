from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GuiaViewSet

router = DefaultRouter()
router.register(r'guias', GuiaViewSet, basename='guia')

urlpatterns = [
    path('', include(router.urls)),
]
