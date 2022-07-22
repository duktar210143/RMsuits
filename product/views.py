from cart.cart import Cart
from product.models import Product
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    product = Product.objects.all()
    return render(request, 'suits/index.html', {'products':product})


@login_required(login_url="/userlogin")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/product")



def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")



def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")



def cart_detail(request):
    return render(request, 'cart/cart_detail.html')