from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart,CartItem
from django.http import JsonResponse
from django.contrib import messages
from a_products.models import Product, Category




def cart_view(request):
    cart = get_object_or_404(Cart, user=request.user)
    categories = Category.objects.filter(parent = None)
    total_price = cart.total_price
    total_discounted_price = cart.total_discounted_price
    discount = total_price - total_discounted_price
    
    context = {
        'cart':cart,
        'discount': discount,
        'categories':categories,
        'range_5': range(5),
    }
    
    return render(request, 'a_cart/cart.html', context)

def add_to_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    
    # Check if the product is already in the cart
    if not cart.items.filter(product=product).exists():
        CartItem.objects.create(
            cart=cart,
            product=product
        )
        messages.success(request, 'Item added to the cart')

    return redirect('cart_view')

def cartitem_remove(request, item_id):
    
    item = get_object_or_404(CartItem, id= item_id)
    
    item.delete()
    messages.success(request, 'Item added to the cart')
    
    return redirect('cart_view')
    
    
def update_cart_item_quantity(request, item_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        cart_item = get_object_or_404(CartItem, id=item_id)

        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        else:
            return redirect('cart_view')

        cart_item.save()
        return redirect('cart_view')

