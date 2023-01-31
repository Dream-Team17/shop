from django.contrib import admin
from core.models import Product, Category, Subcategory, AboutCompany


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "created_date", "updated_date", "available", "discount")
    list_display_links = ("name",)
    search_fields = ("name", "description")
    prepopulated_fields = {'slug': ('name',)}





class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", 'slug')
    list_display_links = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {'slug': ('name',)}



class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "categories")
    list_display_links = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(AboutCompany)
