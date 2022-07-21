
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def login_page(request):
    if request.method=='POST':
        user = authenticate(
            request, 
            username = request.POST['username'],
            password = request.POST['password'],
        )
        if user is not None:
            login(request,user)
            return redirect("")
        else:
            return render("/user/login")
    else:
        return render(request, "users/login.html")

def register_page(request):
    print(request.method)
    if request.method == 'POST':
        User.objects.create_user(
            first_name = request.POST['fullname'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        return redirect("/user/login")
    else:
        return render(request,"users/registerUser.html")

