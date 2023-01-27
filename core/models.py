import os
from datetime import datetime
from uuid import uuid4

from django.db import models


# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'product_images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(datetime.today(), ext)
        # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_rename2(instance, filename):
    upload_to = 'category_images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(datetime.today(), ext)
        # return the whole path to the file
    return os.path.join(upload_to, filename)

def path_and_rename3(instance, filename):
    upload_to = 'subcategory_images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(datetime.today(), ext)
        # return the whole path to the file
    return os.path.join(upload_to, filename)

class Product(models.Model):
    name = models.CharField(max_length=255, help_text="Введите название товара")
    image = models.ImageField(help_text="Загрузите картинку товара", upload_to=path_and_rename)
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
    image = models.ImageField(help_text="Загрузите картинку для категории", upload_to=path_and_rename2)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255, help_text="Введите название подкатегории")
    image = models.ImageField(help_text="Загрузите картинку для подкатегории", upload_to=path_and_rename3)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, help_text="Выберите категорию")

    def __str__(self):
        return self.name



class Company(models.Model):
    description = models.TextField(help_text="Статья или информация о сайте/компании")