# Generated by Django 5.1.3 on 2024-12-06 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.CharField(blank=True, choices=[('home', 'Home'), ('work', 'Work')], default='home', max_length=50, null=True),
        ),
    ]
