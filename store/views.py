from django.shortcuts import get_object_or_404  # -, to get data or 404 error
from django.shortcuts import render

from .models import Category, Product


def products_all(request):  # "products_all" -> name_action
    print("products_all")
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    print("products_detail")
    product = get_object_or_404(Product , slug=slug , in_stock=True)  # Get the object with this slug if it exists
    return render(request, 'store/products/single.html', {'product': product})


def category_list(request, category_slug):
    print('category_list')
    category = get_object_or_404(Category, name=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'products': products, 'category': category})
