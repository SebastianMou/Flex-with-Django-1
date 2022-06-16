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
    print('total')

    # Secret key
    stripe.api_key = 'sk_test_51KFusbLG3Rch548FxCBuH88bWsA2kB3OE261rbEtI0FtiHVrGtZCkMAjkjfJwkqlsCzWfQNxDSQmBzEfawCR6bgg00aWEfvbXH'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='mxn',
        metadata={'userid': request.user.id}
    )
    return render(request, 'Shop/payment/homepay.html', {'client_secret': intent.client_secret})

