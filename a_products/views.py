from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from django.db.models import Q


def get_top_level_categories():
    return Category.objects.filter(parent=None)

def home(request):

    context = {
        'categories':get_top_level_categories(),
        'new_arrivals':Product.objects.all()[:4]
    }
    
    return render(request, 'products/home.html', context)

def category_view(request, category_id):
    
    categories = get_top_level_categories()
    checked_category = get_object_or_404(Category, id=category_id)

    child_categories = Category.objects.filter(
        Q(parent=checked_category) | Q(id=category_id)
    )
    products = Product.objects.filter(category__in=child_categories)

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/category_view.html', context)

def product_view(request, product_id):
    
    product = get_object_or_404(Product, id=product_id)

    product.first_image = product.images.first()
    product_size = product.available_size.split(",")
    
    context = {
        'product':product,
        'product_images': product.images.all(),
        'categories':get_top_level_categories(),
        'product_size':product_size
    }
    return render(request, 'products/product_view.html', context)
