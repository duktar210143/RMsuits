# Generated by Django 4.0.6 on 2022-07-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_order_price_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='suit_price',
            field=models.CharField(max_length=130),
        ),
    ]
