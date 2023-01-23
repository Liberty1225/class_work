from django.shortcuts import render

from .models import Item
from rest_framework import viewsets, generics
from .serializers import ItemSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class ItemListCreateApiView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = ItemSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]



