from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from backend.models.addresses import State, Country, ZipCode
from .serializers import StateSerializer, CountrySerializer, ZipCodeSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticated]

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]

class ZipCodeViewSet(viewsets.ModelViewSet):
    queryset = ZipCode.objects.all()
    serializer_class = ZipCodeSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def autocomplete_address(request):
    query = request.GET.get('q', '').strip()
    if not query:
        return Response([])

    zipcodes = ZipCode.objects.filter(
        Q(city__icontains=query) | Q(code__icontains=query)
    ).values('code', 'city', 'state__abbr', 'country__name')[:10]

    states = State.objects.filter(
        Q(name__icontains=query) | Q(abbr__icontains=query)
    ).values('abbr', 'name')[:5]

    countries = Country.objects.filter(
        Q(name__icontains=query)
    ).values('name', 'state__abbr')[:5]

    results = {
        'zipcodes': list(zipcodes),
        'states': list(states),
        'countries': list(countries),
    }

    return Response(results)
    