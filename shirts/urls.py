from django.urls import path

from shirts import views

urlpatterns = [
    path("",views.shirts)
]