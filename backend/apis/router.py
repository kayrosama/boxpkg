from django.urls import include, path

urlpatterns = [
    path('', include('backend.apis.empresa.router')),
    path('', include('backend.apis.oficina.router')),
    path('', include('backend.apis.catalogos.router')),
    path('', include('backend.apis.direcciones.router')),
    path('', include('backend.apis.addresses.router')),
    path('', include('backend.apis.guias.router')),
]

