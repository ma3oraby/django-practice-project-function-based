from django.shortcuts import render
from .models import Product

# Create your views here.
def products (request) : 
    x = Product.objects.all()
    return render (request,'products/products.html',{'pro':x}) 

def product (request) :
    return render (request,'products/product.html',{'proo':Product.objects.get(id=1)})

  