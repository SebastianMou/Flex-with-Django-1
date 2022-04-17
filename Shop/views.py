from django.shortcuts import get_object_or_404, render
from .models import Category, Product

# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }

def home(request):
    products = Product.objects.all()
    return render(request, 'Shop/home.html', {'products':products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug= slug, in_stock=True)
    products = Product.objects.all()
    return render(request, 'Shop/detail/product_detail.html', {'product': product, 'products':products})