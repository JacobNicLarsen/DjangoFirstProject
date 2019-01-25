from django.shortcuts import render

from .fomrs import ProductForm
from .models import Product

def product_create_veiw(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context ={
        'form': form
    }
    return render(request, "product_detail.html")

def product_detail_veiw(request):
    obj = Product.objects.get(id=1)
    context ={
        'object':obj
    }
    return render(request, "product_detail.html")
