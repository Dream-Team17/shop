# Generated by Django 4.1.5 on 2023-03-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_product_discount_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название вопроса')),
                ('description', models.TextField(verbose_name='Ответ на вопрос')),
                ('faq_slug', models.SlugField(default='', unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Часто задаваемый вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
                'ordering': ('title',),
            },
        ),
    ]
