from django.db import models
import pytils
from .utils import path_and_rename, path_and_rename2, path_and_rename3, count_discount_price



class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Введите название товара", db_index=True)
    product_slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='URl', default='',
                                    help_text="Перед вводом названия продукта очистите это поле")
    image = models.ImageField(help_text="Загрузите картинку товара", upload_to=path_and_rename, blank=True, null=True,
                              default='http://127.0.0.1:8000/media/product_images/11-02-2023_20-39.jpg')
    description = models.TextField(help_text="Введите описание товара", null=True, blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Введите цену")
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, help_text="Выберите категорию")
    subcategories = models.ForeignKey('Subcategory', on_delete=models.CASCADE,
                                      help_text="Выберите подкатегорию")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Скидка в %', null=True,
                                           blank=True, default=0,)
    is_discount = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена со скидкой', null=True,
                                         blank=True, default=0, )

    class Meta:
        ordering = ('name', 'product_slug')
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'product_slug'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.product_slug = pytils.translit.slugify(self.name)
        self.discount_price = count_discount_price(self)
        self.discount_percent = count_discount_price(self)
        super(Product, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=255, help_text="Введите название категории")
    image = models.ImageField(help_text="Загрузите картинку для категории",
                              upload_to=path_and_rename2,
                              blank=True, null=True)
    category_slug = models.SlugField(null=False, db_index=True, unique=True, verbose_name='URl', default='',
                                     help_text="Перед вводом названия категории очистите это поле")

    def save(self, *args, **kwargs):
        self.category_slug = pytils.translit.slugify(self.name)
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
    subcategory_slug = models.SlugField(null=False, db_index=True, unique=True, verbose_name='URl', default='',
                                        help_text="Перед вводом названия подкатегории очистите это поле")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.subcategory_slug = pytils.translit.slugify(self.name)
        super(Subcategory, self).save(*args, **kwargs)
