# Generated by Django 4.1.7 on 2023-03-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, to='products.orderitem'),
        ),
    ]