from django.contrib import admin
from .models import Trait, Listing, Sale

@admin.register(Trait)
class TraitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'listed_date', 'display_traits')
    search_fields = ('title', 'traits__name')
    list_filter = ('traits', 'listed_date')

    def display_traits(self, obj):
        return ", ".join([trait.name for trait in obj.traits.all()])
    display_traits.short_description = 'Traits'

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('display_traits', 'sale_price', 'sale_date', 'pending_sale')
    search_fields = ('traits__name', 'sale_price')
    list_filter = ('traits', 'sale_date', 'pending_sale')

    def display_traits(self, obj):
        return ", ".join([trait.name for trait in obj.traits.all()])
    display_traits.short_description = 'Traits'

