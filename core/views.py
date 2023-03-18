from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Product, Category, Vacant, FAQ
from .serializers import ProductSerializer, CategorySerializer, NewProductSerializer, \
    DiscountProductSerializer, VacantSerializer, FaqSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    lookup_field = 'product_slug'
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name', 'description', 'product_code']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'category_slug'
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name', ]


# class SubcategoryViewSet(viewsets.ModelViewSet):
#     queryset = Subcategory.objects.all()
#     serializer_class = SubcategorySerializer
#     lookup_field = 'subcategory_slug'
#     filter_backends = (DjangoFilterBackend, SearchFilter)
#     search_fields = ('name',)


class NewProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True, is_new=True)
    serializer_class = NewProductSerializer
    lookup_field = 'product_slug'
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name', 'description']


class DiscountProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True).exclude(discount_price=0)
    serializer_class = DiscountProductSerializer
    lookup_field = 'product_slug'
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name', 'description']


class VacantViewSet(viewsets.ModelViewSet):
    queryset = Vacant.objects.all()
    serializer_class = VacantSerializer
    lookup_field = 'vacant_slug'


class FaqViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FaqSerializer
    lookup_field = 'faq_slug'
