from rest_framework import serializers

from apps.apartment_advt.models import ApartmentAdvt


class ApartmentAdvtSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentAdvt
        fields = ('id', 'title', 'price', 'num_of_rooms', 'district', 'short_description')
