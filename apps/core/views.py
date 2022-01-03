from django.shortcuts import render

from apps.product.models import Product

def homepage(request):
    newest_products = Product.objects.all()[0:20]

    return render(request, 'core/homepage.html', {'newest_products': newest_products})


 

