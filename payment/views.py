import stripe
from django.shortcuts import render
from basket.basket import Basket
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    # Secret key
    stripe.api_key = ''
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
    return render(request, 'Shop/payment/homepay.html', {'client_secret': intent.client_secret})

