from django.contrib import admin
from core.models import Product, Category, Subcategory, Company


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "created_data")
    list_display_links = ("name",)
    search_fields = ("name", "description")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "categories")
    list_display_links = ("name",)
    search_fields = ("name",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Company)
