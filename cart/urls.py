from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', views.CartViewSet)
router.register(r'delivery-cost', views.DeliveryCostViewSet)


urlpatterns = router.urls

