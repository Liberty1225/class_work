from .models import Item
from rest_framework import serializers

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
