from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Order, Payment, OrderItem, Delivery

@receiver(post_save, sender=Payment)
def update_order_status(sender, instance, **kwargs):
    if instance.status == "Completed":
        instance.order.status = "Processing"
        instance.order.save()

@receiver(post_save, sender=OrderItem)
@receiver(post_delete, sender=OrderItem)
def update_order_total(sender, instance, **kwargs):
    order = instance.order
    total_price = sum(item.menu_item.price * item.quantity for item in order.orderitem_set.all())
    order.total_price = total_price
    order.save()

@receiver(post_save, sender=Order)
def update_delivery_status(sender, instance, **kwargs):
    delivery, created = Delivery.objects.get_or_create(order=instance)
    
    if instance.status == "Shipped":
        delivery.status = "Shipped"
        delivery.save()
    elif instance.status == "Delivered":
        delivery.status = "Delivered"
        delivery.save()
