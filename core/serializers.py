from rest_framework import serializers
from .models import Product, Category, Subcategory


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(min_value=1)
    discount_percent = serializers.FloatField(min_value=0)
    discount_price = serializers.FloatField(min_value=0)
    weight_volume = serializers.FloatField(min_value=1)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'product_slug', 'image', 'description', 'price', 'categories',
            'subcategories', 'available', 'created_date', 'updated_date', 'is_discount', 'is_new', 'discount_price',
        'discount_percent', 'valid_time', 'weight_volume', 'product_code')


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'category_slug')


class SubcategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'categories', 'subcategory_slug')


class NewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'id', 'name', 'product_slug', 'image', 'description', 'price', 'categories',
            'subcategories', 'available', 'discount_price', 'discount_percent', 'created_date', 'updated_date', 'is_discount', 'is_new')


class DiscountProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'id', 'name', 'product_slug', 'image', 'description', 'price', 'categories',
            'subcategories', 'available', 'discount_price', 'discount_percent', 'created_date', 'updated_date', 'is_discount', 'is_new')