from django.db import models
from decimal import Decimal
from django.templatetags.static import static
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    category_Thumbnail = models.ImageField(upload_to='category_thubnail', blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='subcategories', blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    @property
    def category_image(self):
        if self.category_Thumbnail:
            image =  self.category_Thumbnail.url
        else:
            image = static('images/default_image.png')
            
        return image
    
    def clean(self):
        if self.parent == self:
            raise ValidationError("A category cannot be its own parent.")
    
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
    price = models.DecimalField(max_digits=10, decimal_places=2, default=00.00, validators=[MinValueValidator(Decimal('0.01'))])
    discount = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=1)
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
        price = Decimal(str(self.price))  # Convert price to a Decimal explicitly
        discount_fraction = Decimal(self.discount) / Decimal(100)
        return price - (price * discount_fraction)
    
    def clean(self):
        if self.discount < 0 or self.discount > 100:
            raise ValidationError("Discount must be between 0 and 100.")
    
    def calculate_discounted_price(self):
        price = Decimal(str(self.price))  # Convert self.price to Decimal
        return price - self.discount_price


    def is_stock_low(self, threshold=5):
        return self.stock <= threshold
    
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
    

    