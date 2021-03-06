# Generated by Django 3.1.2 on 2020-11-05 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart_app', '0002_cart_cart_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=256, unique=True)),
                ('order_status', models.CharField(choices=[('Not Yet Shipped', 'Not Yet Shipped'), ('Shipped', 'Shipped'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded'), ('Paid', 'Paid')], default='Not Yet Shipped', max_length=120)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart_app.cart')),
            ],
        ),
    ]
