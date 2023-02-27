from django.contrib import admin
from cart.models import Cart, DeliveryCost


class CartAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")
    list_display_links = ("product",)
    search_fields = ("product", "quantity")

class DeliveryCostAdmin(admin.ModelAdmin):
    list_display = ("name", "cost_per_delivery", "status")
    list_display_links = ("cost_per_delivery",)
    search_fields = ("status", "cost_per_delivery")

admin.site.register(Cart, CartAdmin)
admin.site.register(DeliveryCost, DeliveryCostAdmin)
