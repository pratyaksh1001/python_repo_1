from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path("<int:element>/",views.product_page,name="product_page")
]
