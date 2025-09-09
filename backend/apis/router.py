from django.urls import include, path

urlpatterns = [
    path('', include('backend.apis.empresa.router')),
    path('', include('backend.apis.oficina.router')),
]
