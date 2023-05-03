from django.shortcuts import render
from rest_framework import viewsets
from .models import Country, State, District
from .serializing import CountrySerializer, StateSerializers, DistrictSerializer

# Create your views here.


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StateView(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializers


class DistrictView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


