from django.db import models
from decimal import Decimal
from core.models import Product
from django.conf import settings
from django.db.models import Sum
from django.core.validators import MinLengthValidator


class DeliveryCost(models.Model):
    name = models.CharField(max_length=24, null=False)
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

    def product_name(self):
        return self.product.name

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name

methods = (
    ('наличные', 'Наличные'),
    ('банковской картой при получении', 'Банковской картой при получении'),
    ('mBank', 'mBank'),
)

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.ForeignKey(DeliveryCost, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=32, choices=methods, default='наличные')
    card_number = models.CharField(help_text='введите номер банковской карты(необязательно)', default=690181313,
                                   max_length=9,  validators=[MinLengthValidator(9)], null=True, blank=True)
    number = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=26, null=False)
    delivery_comment = models.TextField(help_text="Комментарии к доставке", null=True, blank=True, default='')

    def __str__(self):
        return self.delivery.name

    def total_price(self):
        return self.cart.total_price() + self.delivery.cost_per_delivery





