from django.shortcuts import render

from .models import Product, Category, Subcategory


def all_products(request):
    """ A view to display all products """
    products = Product.objects.all()


    template = 'product/products.html'
    context = {
        'products': products,
        
    }

    return render(request, template, context)
