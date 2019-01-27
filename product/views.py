from django.shortcuts import render

from .fomrs import ProductForm, RawProductFrom
from .models import Product


# def product_create_view(request):
#     my_form = RawProductFrom()
#     if request.method == "POST":
#         my_form = RawProductFrom(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product_create.html", context)


def product_detail_veiw(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "product_detail.html", context)
