from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User



class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Hot Coffee', 'Drinks'),
        ('Cold COffee', 'drinks'),
        ('Tea', 'dRinks'),
        ('DES', 'Dessert'),
        
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='OTHER')
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links order to a customer
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when order is placed
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Processing', 'Processing'),
                 ('Shipped', 'Shipped'), ('Delivered', 'Delivered')],
        default='Pending'
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def update_total_price(self):
        """ Automatically update total price when Order Items change. """
        self.total_price = sum(item.menu_item.price * item.quantity for item in self.orderitem_set.all())
        self.save()

    def __str__(self):
        return f"Order {self.id} - {self.user.username} ({self.status})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")  # Links to an order
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)  # Links to menu item
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} (Order {self.order.id})"
      
class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)  # Each order has one delivery
    address = models.TextField()  # Customer's delivery address
    status = models.CharField(
        max_length=20,
        choices=[('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Out for Delivery', 'Out for Delivery'),
                 ('Delivered', 'Delivered')],
        default='Processing'
    )
    estimated_delivery = models.DateTimeField(null=True, blank=True)  # Expected arrival time

    def __str__(self):
        return f"Delivery for Order {self.order.id} - {self.status}"
    
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)  # Each order has one payment record
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Stores payment amount
    method = models.CharField(
        max_length=20,
        choices=[('Card', 'Card'), ('UPI', 'UPI'), ('Cash', 'Cash')],
        default='Cash'
    )
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)  # Optional transaction ID
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')],
        default='Pending'
    )

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.status}"
