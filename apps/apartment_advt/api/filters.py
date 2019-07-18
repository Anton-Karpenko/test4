import django_filters as filters

from apps.apartment_advt.models import ApartmentAdvt


class ApartmentAdvtFilter(filters.FilterSet):
    price_lte = filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
    )
    price_gte = filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
    )

    class Meta:
        model = ApartmentAdvt
        fields = ('district', 'num_of_rooms', 'price_lte', 'price_gte')

