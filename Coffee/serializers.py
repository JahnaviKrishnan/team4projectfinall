from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
from .models import Order, OrderItem, Delivery, Payment

class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.StringRelatedField(many=True)  # Show linked items

    class Meta:
        model = Order
        fields = '__all__'
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
