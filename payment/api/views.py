from rest_framework import generics
from payment.models import OnlinePayment
from rest_framework.permissions import AllowAny
from .serializers import OnlinePaymentSerializer


class OentListView(generics.ListAPIView):
    queryset = OnlinePayment.objects.all()
    serializer_class = OnlinePaymentSerializer
    permission_classes = [AllowAny]
    
    def create(self, request):
        print(request.data)