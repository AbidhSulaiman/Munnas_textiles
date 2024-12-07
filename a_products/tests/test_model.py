import pytest
from a_products.models import Product, Category


@pytest.mark.django_db
def test_product():
    category = Category.objects.create(name="category", slug="category")
    product = Product.objects.create(name='product1',category = category,price = 1000.00,discount=10)
    discounted_price = product.discount_price
    
    assert discounted_price == 900
    assert product.calculate_discounted_price() == 100.00
    