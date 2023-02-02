import os
from datetime import datetime

import pytils
from django.db import models

from django.utils.text import slugify

now = datetime.now()


def path_and_rename(instance, filename):
    now = datetime.now()
    upload_to = 'product_images'
    ext = filename.split('.')[-1]

    # set filename as random string
    filename = f'{now.strftime("%d-%m-%Y %H-%M")}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)


def path_and_rename2(instance, filename):
    upload_to = 'category_images'
    ext = filename.split('.')[-1]

    filename = f'{now.strftime("%d-%m-%Y %H-%M")}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)


def path_and_rename3(instance, filename):
    upload_to = 'subcategory_images'
    ext = filename.split('.')[-1]

    # set filename as random string
    filename = f'{now.strftime("%d-%m-%Y %H-%M")}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Введите название товара", db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='URl', default='',
                            help_text="Перед вводом названия продукта очистите это поле")
    image = models.ImageField(help_text="Загрузите картинку товара", upload_to=path_and_rename, blank=True, null=True)
    description = models.TextField(help_text="Введите описание товара", null=True, blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Введите цену")
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, help_text="Выберите категорию")
    subcategories = models.ForeignKey('Subcategory', on_delete=models.CASCADE,
                                      help_text="Выберите подкатегорию")
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    discount = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('name', 'slug')
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = pytils.translit.slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Product, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255, help_text="Введите название категории")
    image = models.ImageField(help_text="Загрузите картинку для категории",
                              upload_to=path_and_rename2,
                              blank=True, null=True)
    slug = models.SlugField(null=False, db_index=True, unique=True, verbose_name='URl', default='',
                            help_text="Перед вводом названия категории очистите это поле")

    def save(self, *args, **kwargs):
        self.slug = pytils.translit.slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255, help_text="Введите название подкатегории")
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, help_text="Выберите категорию")
    slug = models.SlugField(null=False, db_index=True, unique=True, verbose_name='URl', default='',
                            help_text="Перед вводом названия подкатегории очистите это поле")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = pytils.translit.slugify(self.name)
        super(Subcategory, self).save(*args, **kwargs)


class AboutCompany(models.Model):
    description = models.TextField(help_text="Статья или информация о сайте/компании", default='Информация о сайте',
                                   null=True, blank=True)

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'
