from rest_framework import serializers
from .models import Product, Category, Subcategory, AboutCompany


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.HiddenField(default='')

    class Meta:
        model = Product
        fields = (
        'name', 'slug', 'image', 'description', 'price', 'categories', 'subcategories', 'available', 'discount')


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.HiddenField(default='')

    class Meta:
        model = Category
        fields = ('name', 'image', 'slug')


class SubcategorySerializer(serializers.ModelSerializer):
    slug = serializers.HiddenField(default='')

    class Meta:
        model = Subcategory
        fields = ('name', 'categories', 'slug')


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = ('description',)
