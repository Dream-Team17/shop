from django.contrib import admin
from core.models import Product, Category, Subcategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "created_date", "updated_date", "available", "discount_price",
                    "discount_percent")
    list_display_links = ("name",)
    search_fields = ("name", "description")
    prepopulated_fields = {'product_slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", 'category_slug')
    list_display_links = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {'category_slug': ('name',)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "categories")
    list_display_links = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {'subcategory_slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)

