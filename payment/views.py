# import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from orders.tasks import send_sms


# instantiate Braintree payment gateway
# gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        api_key ='30c8bfbb68caae0c'
        secret_key ='NTU1NjJhMjE2ZjVhYzkxZmZlODU1YmRjZGJlZDJlNDgxYTNhYWYzZTkzOTI4MWY4NDE2MDc4NWYxZTZhM2Y1Mg=='
        
        
        result = {
                    'amount': total_cost,
                    'transaction_id': order_id,
                    'reference_number': 'SOKO-12345',
                    'mobile': request.get('phone'),
                }
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
           
            order.save()
            return redirect('done')
        else:
            return redirect('canceled')
    else:
 
        return render(request,
                      'payment/process.html',
                      {'order': order,
                       'total_cost':total_cost,
                       'order_id':order_id
                    #    'client_token': client_token
                    })


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
