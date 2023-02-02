from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Product, Category, Subcategory, AboutCompany
from .serializers import ProductSerializer, CategorySerializer, SubcategorySerializer, AboutCompanySerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name', 'description']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name', ]


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name',)


class AboutCompanyViewSet(viewsets.ModelViewSet):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer
    lookup_field = 'slug'
