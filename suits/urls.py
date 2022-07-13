from django.urls import URLPattern, path
from suits import views

urlpatterns = [
    path("",views.index),
    path("/details",views.details)
]