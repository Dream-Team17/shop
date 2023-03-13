from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'subcategories', views.SubcategoryViewSet)
router.register(r'new-products', views.NewProductViewSet)
router.register(r'discount-products', views.DiscountProductViewSet)
router.register(r'vacants', views.VacantViewSet)

urlpatterns = router.urls
