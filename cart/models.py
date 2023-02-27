from django.db import models
from decimal import Decimal
from core.models import Product
from django.conf import settings
# Create your models here.
class DeliveryCost(models.Model):
    name = models.CharField(max_length=9,
                            choices=(('Globus', 'Globus'), ('Narodnyi', 'Narodnyi')),)
    status = models.CharField(max_length=7,
                              choices=(('Active', 'active'), ('Passive', 'passive')),
                              default="passive",
                              null=False)
    cost_per_delivery = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fixed_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                help_text='Добавить Продукт', verbose_name='Продукт')
    quantity = models.IntegerField(null=False, verbose_name='Количество Товара')
    delivery_cost = models.ForeignKey(DeliveryCost, on_delete=models.CASCADE)

    @property
    def product_name(self):
        return self.product.name

    @property
    def total_price(self):
        return self.product.price * self.quantity

    @property
    def delivery_company(self):
        return self.delivery_cost.name

    @property
    def cost_delivery(self):
        return self.delivery_cost.cost_per_delivery


    def __str__(self):
        return self.product.name

