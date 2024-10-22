from .models import Manufacturer, Car
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import ManufacturerSerializer, CarSerializer


# Read
class ManufacturerListView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# Create
class ManufacturerCreateView(CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CarCreateView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# Update/Delete
class ManufacturerReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CarReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
