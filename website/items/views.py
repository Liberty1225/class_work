from django.shortcuts import render

from .models import Item
from rest_framework import viewsets, generics
from .serializers import ItemSerializers


class ItemListCreateApiView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = ItemSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]



