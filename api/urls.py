from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TraitViewSet, ListingViewSet, SaleViewSet

router = DefaultRouter()
router.register(r'traits', TraitViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
