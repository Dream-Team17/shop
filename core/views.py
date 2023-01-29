from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


class SearchViewPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'  # client can regulate pagination limit page_size = ?
    max_page_size = 10000  # the limit of page_size_query_param e.g. client cant enter number more than 10000


class SearchView(ListAPIView):
    queryset = Product.objects.all()
    for query in queryset:
        query.save()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['name', 'description']
    pagination_class = SearchViewPagination


class ProductDetailCBV(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, slug_product=None, **kwargs):
        products = self.queryset.get(slug=slug_product)
        serializer = ProductSerializer(products)
        return Response(data=serializer.data)
