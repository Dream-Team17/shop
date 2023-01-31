# Generated by Django 4.1.5 on 2023-01-29 18:02

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название категории', max_length=255)),
                ('image', models.ImageField(help_text='Загрузите картинку для категории', upload_to=core.models.path_and_rename2)),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Статья или информация о сайте/компании')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название подкатегории', max_length=255)),
                ('image', models.ImageField(help_text='Загрузите картинку для подкатегории', upload_to=core.models.path_and_rename3)),
                ('slug', models.SlugField(default='')),
                ('categories', models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название товара', max_length=255)),
                ('image', models.ImageField(help_text='Загрузите картинку товара', upload_to=core.models.path_and_rename)),
                ('description', models.TextField(help_text='Введите описание товара')),
                ('price', models.DecimalField(decimal_places=2, help_text='Введите цену', max_digits=10)),
                ('created_data', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(default='')),
                ('categories', models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('subcategories', models.ForeignKey(blank=True, help_text='Выберите подкатегорию', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.subcategory')),
            ],
        ),
    ]
