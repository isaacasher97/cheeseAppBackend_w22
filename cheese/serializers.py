from .models import Cheese
from rest_framework import serializers

# Cheese Serializer
class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #models to serialize
        model = Cheese
        #fields to show in json
        fields = ('id', 'name', 'origin_country', 'typeOfCheese')