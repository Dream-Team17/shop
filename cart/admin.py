from django.contrib import admin
from cart.models import Cart, DeliveryCost, Order


class CartAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")
    list_display_links = ("product",)
    search_fields = ("product", "quantity")

class DeliveryCostAdmin(admin.ModelAdmin):
    list_display = ("name", "cost_per_delivery", "status")
    list_display_links = ("cost_per_delivery",)
    search_fields = ("status", "cost_per_delivery")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("number", "address")
    list_display_links = ("number",)
    search_fields = ("number", "address", "card_number")

admin.site.register(Cart, CartAdmin)
admin.site.register(DeliveryCost, DeliveryCostAdmin)
admin.site.register(Order, OrderAdmin)

