from rest_framework import serializers
from .models import Cart, DeliveryCost

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product', 'product_name', 'quantity', 'total_price',
                  'delivery_cost', 'delivery_company', 'cost_delivery']

class DeliveryCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCost
        fields = ['id', 'name', 'status', 'cost_per_delivery', 'fixed_cost']