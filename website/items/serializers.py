from .models import Item
from rest_framework import serializers


class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ['count']


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
