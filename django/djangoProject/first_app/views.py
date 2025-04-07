from django.shortcuts import render,get_object_or_404
from .models import first_model
print(first_model.objects.all())


def home(request):
    data={
        "my_data":first_model.objects.all()
    }
    return render(request,"first_app/first_home.html",data)


def product_page(request,element):
    product_details=get_object_or_404(first_model,pk=element)
    return render(request,"first_app/product.html", {"data":product_details})