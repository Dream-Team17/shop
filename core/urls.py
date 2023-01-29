from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchView.as_view()),
    path('<slug:slug_product>', views.ProductDetailCBV.as_view()),
]
