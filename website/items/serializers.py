from .models import Item
from rest_framework import serializers


class ItemSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    count = serializers.IntegerField()

    def create(self, validated_data):
        item = Item.objects.create(**validated_data)
        return item
