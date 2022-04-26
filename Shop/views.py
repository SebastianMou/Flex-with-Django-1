from django.shortcuts import get_object_or_404, render
from .models import Category, Product

# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }

def home(request):
    products = Product.products.all()
    return render(request, 'Shop/home.html', {'products':products})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'Shop/products/category.html', {'category': category, 'products': products}) 

def product_detail(request, slug):
    product = get_object_or_404(Product, slug= slug, in_stock=True)
    products = Product.objects.all()
    return render(request, 'Shop/products/single.html', {'product': product, 'products':products})