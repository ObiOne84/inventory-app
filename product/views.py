from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Product, Category, Subcategory


def all_products(request):
    """ A view to display all products """
    products = Product.objects.all()

    paginator = Paginator(products, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    max_page_number = 5
    current_page = page_obj.number
    total_pages = paginator.num_pages

    start_page = max(1, current_page - (max_page_number // 2))
    end_page = min(total_pages, start_page + max_page_number -1)

    if end_page - start_page + 1 < max_page_number:
        start_page = max(1, end_page - max_page_number + 1)
    page_range = range(start_page, end_page + 1)

    is_paginated = paginator.count > 30

    template = 'product/products.html'
    context = {
        'products': products,
        'is_paginated': is_paginated,
        'page_obj': page_obj,
        'page_range': page_range,
        
    }

    return render(request, template, context)
