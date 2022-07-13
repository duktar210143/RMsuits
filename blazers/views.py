from django.shortcuts import render

# Create your views here.
def blazers(request):
    return render(request,"Blazers/index.html")