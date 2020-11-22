# Generated by Django 3.1.2 on 2020-11-01 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0006_product_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
