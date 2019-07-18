from django.urls import path

from apps.apartment_advt.api.views import ListApartmentAdvtAPIView

app_name = "apartment_advt"

urlpatterns = [
    path('', ListApartmentAdvtAPIView.as_view(), name='advertises'),
]
