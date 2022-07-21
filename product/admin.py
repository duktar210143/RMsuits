from django.contrib import admin
from product.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','suit_name','suit_price','suit_brand','suit_desc','suit_image')

admin.site.register(Product,ProductAdmin)
