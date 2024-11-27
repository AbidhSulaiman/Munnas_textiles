from django.db import models
from django.contrib.auth.models import User
from a_products.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())
    @property
    def total_discounted_price(self):
        return sum(item.total_discounted_price for item in self.items.all())

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    def __str__(self):
        return f"Cart for {self.user.username if self.user else 'Guest'}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    

    @property
    def total_price(self):
        return self.quantity * self.product.price
    @property
    def total_discounted_price(self):
        return self.quantity * self.product.discount_price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"