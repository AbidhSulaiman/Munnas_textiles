from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from django.db.models import Q

def home(request):
    
    categories = Category.objects.filter(parent = None)
    new_arrivals = Product.objects.all()[:4]

    context = {
        'categories':categories,
        'new_arrivals':new_arrivals
    }
    
    return render(request, 'products/home.html', context)

def category_view(request, category_id):
    
    categories = Category.objects.filter(parent = None)
    
    checked_category = Category.objects.get(id = category_id)
    
    child_categories = Category.objects.filter(Q(parent=checked_category) | Q(id=category_id))
    
    products = Product.objects.filter(category__in=child_categories)
           
    context = {
        'products':products,
        'categories':categories
    }
    return render(request, 'products/category_view.html', context)

def product_view(request, product_id):
    
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.filter(parent = None)

    product.first_image = product.images.first()
    product_size = product.available_size.split(",")
    
    context = {
        'product':product,
        'product_images': product.images.all(),
        'categories':categories,
        'product_size':product_size
    }
    return render(request, 'products/product_view.html', context)
