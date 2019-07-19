from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters
from rest_framework import generics

from apps.apartment_advt.api import docs
from apps.apartment_advt.models import ApartmentAdvt
from .filters import ApartmentAdvtFilter
from .serializers import ApartmentAdvtSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(**docs.list_apartment_advertises))
class ListApartmentAdvtAPIView(generics.ListAPIView):
    serializer_class = ApartmentAdvtSerializer
    queryset = ApartmentAdvt.objects.all()
    filter_backends = DjangoFilterBackend, filters.SearchFilter
    filterset_class = ApartmentAdvtFilter
    search_fields = 'description', 'title'
