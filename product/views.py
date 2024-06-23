from django.shortcuts import render


def all_products(request):
    """ A view to display all products """

    template = 'product/products.html'
    context = {
        
    }

    return render(request, template, context)
