from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"suits/index.html")

def details(request):
    return render(request,"suits/suits-details.html")

