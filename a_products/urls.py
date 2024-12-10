from django.urls import path
from .views import home, category_view, product_view, search_product

urlpatterns = [
    path('',home, name='home'),
    path('category_view/<category_id>/',category_view, name='category_view'),
    path('product_view/<product_id>/',product_view, name='product_view'),
    path('search_product/',search_product, name='search_product'),
]
