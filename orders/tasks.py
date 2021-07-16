from celery import task
from django.core.mail import send_mail
from .models import Order
from django.conf import settings
import json
import requests


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
        f'You have successfully placed an order.' \
        f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                                  message,
                                  'dex90jay@gmail.com',
                                  [order.email])
    return mail_sent

# def orderplaced(order_id, customer_name, customer_phone, delivery_addr):
#     #message_to_broadcast = (
#         #f'We have received your request {customer_name.capitalize()},from {delivery_addr}, {customer_phone}, Your order number is {order_id}')
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
#     message_to_broadcast_customer = (
#         f'Contact: {customer_phone}. We have received your request {customer_name.capitalize()},from {delivery_addr}. Your order number is {order_id}')

#     send_sms = client.messages.create(to=customer_phone,
#                            from_=settings.TWILIO_NUMBER,
#                            body=message_to_broadcast_customer)
    
    
#     return send_sms

def send_sms(order_id, customer_name, delivery_addr, customer_phone):
    URL = 'https://apisms.beem.africa/v1/send'
    api_key ='api_key'
    secret_key = 'secret_key'
    content_type = 'application/json'
    source_addr = 'Kanyasu'
    apikey_and_apisecret = api_key + ':' + secret_key

    first_request = requests.post(url = URL,data = json.dumps({
    'source_addr': source_addr,
    'schedule_time': '',
    'encoding': '0',
    'message': f"Hello, We have received your request {customer_name}, from {delivery_addr}, your number is {customer_phone}, and your Order ID is {order_id},You can now Pay Securely",
    'recipients': [
    {
    'recipient_id': 1,
    'dest_addr': '255752585587',
    },
    ],
    }),
        
    headers = {
    'Content-Type': content_type,
    'Authorization': 'Basic ' + api_key + ':' + secret_key,
    },
    auth=(api_key,secret_key),verify=False)

    print(first_request.status_code)
    print(first_request.json())
    return (first_request.json())
            
    @app.errorhandler(500)
    def server_error(e):
        errorName='Error'
        return Response(
            json.dumps(errorName),
            status=500,
            )
        return send_sms
                
                
