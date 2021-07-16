from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
# from twilio.rest import Client
from .tasks import send_sms
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         vendor=item['product'].vendor,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                
                order.vendors.add(item['product'].vendor)
                order=order
                order_id = order.id
                customer_name = order.first_name
                delivery_addr = order.address   
                customer_phone = order.phone_number
                
            # clear the cart
            cart.clear()
            # launch asynchronous task
            send_sms(order_id=order.id, customer_name=customer_name,delivery_addr=delivery_addr, customer_phone=customer_phone)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('process'))
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
            
    else:
        form = OrderCreateForm()
        return render(request,
                      'orders/order/create.html',
                      {'cart': cart, 'form': form})
        

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


        
        
@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + 'css/pdf.css')])
    return response