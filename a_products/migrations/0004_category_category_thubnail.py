# Generated by Django 5.1.3 on 2024-11-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_products', '0003_alter_product_options_alter_productimage_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_thubnail',
            field=models.ImageField(blank=True, null=True, upload_to='category_thubnail'),
        ),
    ]