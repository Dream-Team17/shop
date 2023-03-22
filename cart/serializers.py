from rest_framework import serializers
from .models import Cart, DeliveryCost, Order
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product', 'product_name', 'quantity', 'total_price' ]
class DeliveryCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCost
        fields = ['id', 'name', 'status', 'cost_per_delivery', 'fixed_cost']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'cart', 'delivery', 'number', 'address', 'delivery_comment', 'total_price', 'payment_method',
                  'card_number']