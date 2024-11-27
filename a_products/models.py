from django.db import models
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    category_thubnail = models.ImageField(upload_to='category_thubnail', blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='subcategories', blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    discount = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)
    available_size = models.CharField(max_length=250, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name} - {self.category}'
    
    def get_first_image(self):
        first_image = self.images.first()
        return first_image.image.url if first_image else None
    
    @property
    def discount_price(self):
        discount_fraction = Decimal(self.discount) / Decimal(100)
        return self.price - (self.price * discount_fraction)
    
    class Meta:
        verbose_name_plural = "Products"
        ordering = ["-created_at"]
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Image for {self.product.name}"
    
    class Meta:
        verbose_name_plural = "ProductImages"
    

    