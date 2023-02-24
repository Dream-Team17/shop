from rest_framework import serializers
from .models import Product, Category, Subcategory


class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = (
            'id', 'name', 'product_slug', 'image', 'description', 'price', 'categories',
            'subcategories', 'available', 'discount', 'created_date', 'updated_date', 'is_discount', 'is_new')


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
            'subcategories', 'available', 'discount', 'created_date', 'updated_date', 'is_discount', 'is_new')


class DiscountProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'id', 'name', 'product_slug', 'image', 'description', 'price', 'categories',
            'subcategories', 'available', 'discount', 'created_date', 'updated_date', 'is_discount', 'is_new')