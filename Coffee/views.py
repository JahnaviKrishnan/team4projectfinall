from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem
from rest_framework import viewsets
from .models import MenuItem, Order, Delivery, Payment
from .serializers import MenuItemSerializer, OrderSerializer, DeliverySerializer, PaymentSerializer
# Create your views here.
def home(request):
    coffee_items = MenuItem.objects.all()
    return render(request, 'home.html', {'coffee_items': coffee_items})


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
