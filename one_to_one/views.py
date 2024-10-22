from .models import House, Family
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import HouseSerializer, FamilySerializer


# Read
class HouseListView(ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class FamilyListView(ListAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


# Create
class HouseCreateView(CreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class FamilyCreateView(CreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


# Update/Delete
class HouseReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class FamilyReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
