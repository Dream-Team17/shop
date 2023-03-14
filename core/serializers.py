from rest_framework import serializers
from .models import Product, Category, Subcategory, Vacant, FAQ


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'category_slug')


class SubcategorySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=False)

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'categories', 'subcategory_slug')


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(min_value=1)
    # discount = serializers.FloatField(min_value=0)
    discount_price = serializers.FloatField(min_value=0)
    weight_volume = serializers.FloatField(min_value=1)
    categories = CategorySerializer(many=False)
    subcategories = SubcategorySerializer(many=False)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'product_slug', 'image', 'description', 'price', 'categories',
            'subcategories', 'available', 'created_date', 'updated_date', 'is_new', 'discount_price',
            'valid_time', 'weight_volume', 'product_code')


class NewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_slug', 'image', 'description', 'price', 'categories',
                  'subcategories', 'available', 'discount_price', 'created_date', 'updated_date', 'is_new')


class DiscountProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_slug', 'image', 'description', 'price', 'categories',
                  'subcategories', 'available', 'discount_price', 'created_date', 'updated_date', 'is_new')


class VacantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacant
        fields = ('id', 'title', 'vacant_slug', 'salary', 'conditions', 'information', 'duties', 'requirements',
                  'additional', 'key_skills')


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('id', 'faq_slug', 'title', 'description')
