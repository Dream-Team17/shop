from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Cart, DeliveryCost
from .serializers import CartSerializer, DeliveryCostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['product', 'quantity']

class DeliveryCostViewSet(viewsets.ModelViewSet):
    queryset = DeliveryCost.objects.all()
    serializer_class = DeliveryCostSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name', 'cost_per_delivery']

