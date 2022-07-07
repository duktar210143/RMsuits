from pydoc import importfile
from django.urls import include,path
from home import views

urlpatterns=[
    path("",views.index),
    path("suits",views.suits),

]

