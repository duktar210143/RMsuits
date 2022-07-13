from django.shortcuts import render

# Create your views here.

def shirts(request):
    return render(request,"shirts/index.html")