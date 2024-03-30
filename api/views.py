from django.shortcuts import render
from rest_framework import generics


# Create your views here.
from .models import Item,Location
from .serializers import ItemSerializers,LocationSerializers

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializers

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemLocation=location)
        return queryset

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializers
    queryset = Item.objects.all()

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializers
    queryset = Location.objects.all()

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializers
    queryset = Location.objects.all()




    
    