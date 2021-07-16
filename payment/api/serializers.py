from rest_framework import serializers
from payment.models import OnlinePayment

class OnlinePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlinePayment
        fields = ['id']