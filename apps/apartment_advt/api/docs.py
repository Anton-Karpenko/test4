from drf_yasg import openapi


price_lte = openapi.Parameter(
    'price_lte',
    openapi.IN_QUERY,
    description="Price less than or equals",
    type=openapi.TYPE_INTEGER,
)

price_gte = openapi.Parameter(
    'price_gte',
    openapi.IN_QUERY,
    description="Price greater than or equals",
    type=openapi.TYPE_INTEGER,
)

district = openapi.Parameter(
    'district',
    openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    enum=['Борщаговка', 'Голосеевский', 'Дарницкий', 'Деснянский', 'Днепровский', 'Оболонский', 'Печерский',
          'Подольский', 'Святошинский', 'Соломенский', 'Шевченковский', 'Троещина']
)

list_apartment_advertises = {
    'manual_parameters': [district, price_gte, price_lte]
}
