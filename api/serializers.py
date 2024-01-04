from rest_framework import serializers
from .models import Trait, Listing, Sale

class TraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trait
        fields = ['id', 'name', 'description']

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'traits', 'title', 'price', 'listed_date', 'image_url']

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'traits', 'sale_price', 'sale_date', 'pending_sale']
