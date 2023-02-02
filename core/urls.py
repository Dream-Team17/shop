from django.urls import path
from . import views

urlpatterns = [

    path('products/', views.ProductViewSet.as_view({'get': 'list',
                                                    'post': 'create'})),
    path('products/<str:slug>/', views.ProductViewSet.as_view({'get': 'retrieve',
                                                               'put': 'update',
                                                               'delete': 'destroy'})),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list',
                                                       'post': 'create'})),
    path('categories/<str:slug>/', views.CategoryViewSet.as_view({'get': 'retrieve',
                                                                  'put': 'update',
                                                                  'delete': 'destroy'})),
    path('subcategories/', views.SubcategoryViewSet.as_view({'get': 'list',
                                                             'post': 'create'})),
    path('subcategories/<str:slug>/', views.SubcategoryViewSet.as_view({'get': 'retrieve',
                                                                        'put': 'update',
                                                                        'delete': 'destroy'})),
    path('aboutcompany/', views.AboutCompanyViewSet.as_view({'get': 'list',
                                                             'post': 'create', })),
]
