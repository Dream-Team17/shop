from django.urls import path
from . import views

get_post = {'get': 'list',
            'post': 'create'}
get_put_delete = {'get': 'retrieve',
                  'put': 'update',
                  'delete': 'destroy'}
urlpatterns = [

    path('products/', views.ProductViewSet.as_view(get_post)),
    path('products/<str:slug>/', views.ProductViewSet.as_view(get_put_delete)),
    path('categories/', views.CategoryViewSet.as_view(get_post)),
    path('categories/<str:slug>/', views.CategoryViewSet.as_view(get_put_delete)),
    path('subcategories/', views.SubcategoryViewSet.as_view(get_post)),
    path('subcategories/<str:slug>/', views.SubcategoryViewSet.as_view(get_put_delete)),
    path('aboutcompany/', views.AboutCompanyViewSet.as_view(get_post)),
]
