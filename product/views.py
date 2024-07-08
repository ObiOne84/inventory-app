from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models.functions import Lower

from .models import Product


def all_products(request):
    """ A view to display all products """
    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if query:
                queries = (
                    Q(title__icontains=query)
                )
                products = products.filter(queries)
                if len(products) == 0:
                    messages.error(request, f"Sorry, we didn't \
                        find any product matching '{query}'.")
                    return redirect(reverse('products'))
            else:
                messages.error(request, "You didn't enter any \
                    search criteria!")
                return redirect(reverse('products'))
        if query is not None:
            messages.success(request, f"You are viewing \
                results for '{query}'.")

    # products = products.order_by('id')

    paginator = Paginator(products, 30)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    max_page_number = 5
    current_page = page_obj.number
    total_pages = paginator.num_pages

    start_page = max(1, current_page - (max_page_number // 2))
    end_page = min(total_pages, start_page + max_page_number - 1)

    if end_page - start_page + 1 < max_page_number:
        start_page = max(1, end_page - max_page_number + 1)
    page_range = range(start_page, end_page + 1)

    is_paginated = paginator.count > 30
    current_sorting = f'{sort}_{direction}'

    # if request.is_ajax():
    #     return render(request, 'product/
    # product_list_content.html', {'page_obj': page_obj})

    template = 'product/products.html'
    context = {
        'products': products,
        'is_paginated': is_paginated,
        'page_obj': page_obj,
        'page_range': page_range,
        'start_page': start_page,
        'end_page': end_page,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = Product.objects.get(id=product_id)

    template = 'product/product_detail.html'
    context = {
        'product': product,
    }

    return render(request, template, context)
