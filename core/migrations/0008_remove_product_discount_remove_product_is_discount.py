# Generated by Django 4.1.5 on 2023-03-14 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_vacant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_discount',
        ),
    ]
