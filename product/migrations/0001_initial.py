# Generated by Django 4.0.6 on 2022-07-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('suit_name', models.CharField(max_length=120)),
                ('suit_price', models.FloatField(blank=True)),
                ('suit_brand', models.CharField(blank=True, max_length=100)),
                ('suit_desc', models.CharField(blank=True, max_length=2000)),
                ('suit_image', models.FileField(default='default.jpg', upload_to='static/image')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]