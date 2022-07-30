from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Category, Product, CategoryPlantillas, ProductPlantillas
from django.core.paginator import Paginator

# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }

def categoriesplantillas(request):
    return {
        'categoriesplantillas': CategoryPlantillas.objects.all()
    }

def home(request):
    products = Product.products.all()
    return render(request, 'Shop/home.html', {'products':products})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'Shop/products/category.html', context) 

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    products = Product.objects.all()
    context = {
        'product': product,
        'products': products,
    }
    return render(request, 'Shop/products/single.html', context)

def freelancer(request):
    data = Product.objects.all()
    p = Paginator(data, 6)
    page = request.GET.get('page')
    article = p.get_page(page)
    context = {
        'data': data,
        'article': article,
    }
    return render(request, 'Shop/allproducts/freelance_services.html', context)

def plantillas(request):
    productplantillas = ProductPlantillas.objects.all()
    context = {
        'productplantillas': productplantillas,
    }
    return render(request, 'Shop/allproducts/plantillas.html', context)

def plantillas_detail(request, plantillas_slug):
    productplantilla = get_object_or_404(ProductPlantillas, slug_p=plantillas_slug, in_stock_p=True)
    productplantillas = ProductPlantillas.objects.all()
    context = {
        'productplantilla': productplantilla,
        'productplantillas': productplantillas,
    }
    return render(request, 'Shop/products/plantilla_single.html', context)

def plantilla_category_list(request, plantilla_category_slug=None):
    category_plantillas = get_object_or_404(CategoryPlantillas, slug_p=plantilla_category_slug)
    plantillas = ProductPlantillas.objects.filter(category_plantillas=category_plantillas)
    context = {
        'category_plantillas': category_plantillas,
        'plantillas': plantillas,
    }
    return render(request, 'Shop/products/plantilla_category.html', context)