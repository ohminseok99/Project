from django.shortcuts import render, get_object_or_404
from product.models import Product

def index(request, product_id=None):
    product = get_object_or_404(Product, id=product_id)
    return render(request,'detail.html', {'email' : request.session.get('user'), 'product' : product})