# Generated by Django 5.1.3 on 2024-12-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_products', '0006_rename_category_thubnail_category_category_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=1),
        ),
    ]