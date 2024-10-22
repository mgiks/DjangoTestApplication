from rest_framework import serializers
from .models import House
from .models import Family


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ["lastname", "number_of_members"]