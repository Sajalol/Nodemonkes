from rest_framework import viewsets
from .models import Trait, Listing, Sale
from .serializers import TraitSerializer, ListingSerializer, SaleSerializer

class TraitViewSet(viewsets.ModelViewSet):
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
