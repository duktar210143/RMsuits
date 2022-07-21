from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    suit_name = models.CharField(max_length=120)
    suit_price = models.FloatField(blank=True)
    suit_brand = models.CharField(max_length=100,blank=True)
    suit_desc = models.CharField(max_length=2000,blank=True)
    suit_image = models.FileField(upload_to="static/image",default="default.jpg")

    class Meta:
        db_table = "product"