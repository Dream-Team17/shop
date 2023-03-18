from django.contrib import admin
from core.models import Product, Category,Vacant, FAQ


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "created_date", "updated_date", "available", "discount_price")
    list_display_links = ("name",)
    search_fields = ("name", "description")
    prepopulated_fields = {'product_slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", 'category_slug')
    list_display_links = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {'category_slug': ('name',)}


# class SubcategoryAdmin(admin.ModelAdmin):
#     list_display = ("name", "categories")
#     list_display_links = ("name",)
#     search_fields = ("name",)
#     prepopulated_fields = {'subcategory_slug': ('name',)}


class VacantAdmin(admin.ModelAdmin):
    list_display = ('title', 'vacant_slug')
    list_display_links = ('title',)
    search_fields = ("title",)
    prepopulated_fields = {'vacant_slug': ('title',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Vacant, VacantAdmin)
admin.site.register(FAQ)
