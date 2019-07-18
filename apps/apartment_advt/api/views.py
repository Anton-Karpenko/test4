from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics

from apps.apartment_advt.models import ApartmentAdvt
from .filters import ApartmentAdvtFilter
from .serializers import ApartmentAdvtSerializer


class ListApartmentAdvtAPIView(generics.ListAPIView):
    serializer_class = ApartmentAdvtSerializer
    queryset = ApartmentAdvt.objects.all()
    filter_backends = DjangoFilterBackend, filters.SearchFilter
    filterset_class = ApartmentAdvtFilter
    search_fields = 'description', 'title'
