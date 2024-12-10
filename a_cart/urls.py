from django.urls import path
from .views import cart_view, add_to_cart, cartitem_remove, update_cart_item_quantity, update_cart_item_size

urlpatterns = [
    path('cart_view/', cart_view, name='cart_view'),
    path('add_to_cart/<product_id>', add_to_cart, name='add_to_cart'),
    path('cartitem_remove/<item_id>', cartitem_remove, name='cartitem_remove'),
    path('update_cart_quantity/<item_id>', update_cart_item_quantity, name='update_cart_item_quantity'),
    path('update-cart-item-size/<int:item_id>/', update_cart_item_size, name='update_cart_item_size'),
]