from rest_framework import serializers
from .models import Product, Category, Company, Subcategory


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ' id name description  categories image'.split()

    def get_categories(self, instance):
        return instance.categories.name
