from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse

from Shop.models import Product
from .basket import Basket

# Create your views here.

def basket_summary(request):
    basket = Basket(request)
    return render(request, 'Shop/basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        ##product_qty = int(request.POST.get('productqty'))
        try:
            product = Product.objects.get(id=product_id) 
        except:
            raise Http404                                
        ##basket.add(product=product, qty=product_qty)
        basket.add(product=product, qty=1)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response

'''

from django.http import Http404, JsonResponse
from django.shortcuts import render
from Shop.models import Product
from .basket import Basket

# Create your views here.
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'Shop/basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        #product_qty = int(request.POST.get('productqty'))
        #product = get_object_or_404(Product, id=product_id)
        try:
            product = Product.objects.get(id=product_id) 
        except:
            raise Http404 
        basket.add(product=product, qty=1)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        response = JsonResponse({'Success': True})
        return response


'''