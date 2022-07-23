from audioop import add
from unicodedata import name
from cart.cart import Cart
from product.models import Product, Order
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from order.models import Order


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

def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)

        print(address,phone,cart,user)
        for i in cart:
            print(i)
            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                phone = phone,            )
            order.save()
        return redirect("/product")


    return HttpResponse("this is checkout page")