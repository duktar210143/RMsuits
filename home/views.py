from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"Home/index.html")



def suits(request):
    return render(request,"suits/index.html")