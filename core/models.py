from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, help_text="Введите название товара")
    image = models.ImageField(help_text="Загрузите картинку товара")
    description = models.TextField(help_text="Введите описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Введите цену")
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, help_text="Выберите категорию")
    subcategories = models.ForeignKey('Subcategory', on_delete=models.CASCADE, null=True, blank=True,
                                      help_text="Выберите подкатегорию")
    created_data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, help_text="Введите название категории")
    image = models.ImageField(help_text="Загрузите картинку для категории")

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255, help_text="Введите название подкатегории")
    image = models.ImageField(help_text="Загрузите картинку для подкатегории")
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, help_text="Выберите категорию")

    def __str__(self):
        return self.name


class Company(models.Model):
    description = models.TextField(help_text="Статья или информация о сайте/компании")
