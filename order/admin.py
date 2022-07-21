from django.contrib import admin

from order.models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','product','user','quantity','price','address','phone','date')

admin.site.register(Order,OrderAdmin)
