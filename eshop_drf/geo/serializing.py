from rest_framework import serializers
from .models import Country, State, District


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializers(serializers.ModelSerializer):
    country = serializers.StringRelatedField(source='country.name')

    class Meta:
        model = State
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    state = serializers.StringRelatedField(source='state.name')

    class Meta:
        model = District
        fields = '__all__'
