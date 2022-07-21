import datetime
from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.

class Order(models.Model):
    image = models.ImageField(upload_to='ecommerce/order/image')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.CharField(max_length=5)
    price = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=13)
    date = models.DateField(default = datetime.datetime.today)

    class Meta:
        db_table = "Order"
    
    def __str__(self):
        return self.product.suit_name
