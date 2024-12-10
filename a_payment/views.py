from django.shortcuts import render
from a_products.models import Product, Category
from a_cart.models import CartItem

# Create your views here.

def payment(request, id):
    
    cart_item = CartItem.objects.get(id = id)
    
    user = request.user
    first_address = user.profile.address.first()
    full_address = first_address.address +" "+ first_address.city +" "+ first_address.state
    
    context = {
        'cart_item':cart_item,
        'range_5': range(5),
        'full_address':full_address
        
        }
    
    
    return render(request, 'a_payment/paymentpage.html', context)
