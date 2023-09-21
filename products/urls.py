from django.urls import path
from .views import  products , product

urlpatterns = [
    path('',products,name='products.html'),
    path('product',product,name='product.html'),
]
