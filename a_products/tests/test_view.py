import pytest
from django.urls import reverse
from a_products.models import Product, Category


@pytest.fixture
def category_data():
    parent_category = Category.objects.create(name="parent_category", slug="parent-category")
    child_category = Category.objects.create(name="child_category", slug="child-category", parent=parent_category)
    product_one = Product.objects.create(name="product_one", category=child_category, price=99.99, discount=5, available_size='S,M,L')
    product_two = Product.objects.create(name="product_two", category=child_category, price=99.99, discount=5)
    
    return parent_category, child_category, product_one, product_two

@pytest.mark.django_db
def test_category_view(client, category_data):
    parent_category, child_category, product_one, product_two = category_data
    
    response = client.get(reverse('category_view', args=[parent_category.id]))
    
    assert response.status_code == 200
    
    assert 'products' in response.context
    assert 'categories' in response.context
    
    products_in_context = list(response.context['products'])
    assert product_one in products_in_context
    assert product_two in products_in_context
    
    assert parent_category in response.context['categories']
    
    assert 'products/category_view.html' in [t.name for t in response.templates]
    
@pytest.mark.django_db
def test_product_view(client, category_data):
    parent_category, child_category, product_one, _ = category_data
    
    response = client.get(reverse('product_view', args=[product_one.id]))
    
    assert response.status_code == 200
    
    assert 'product' in response.context
    assert response.context['product'] == product_one
    
    assert 'product_size' in response.context
    assert response.context['product_size'] == ['S', 'M', 'L']