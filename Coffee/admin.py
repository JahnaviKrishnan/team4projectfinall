from django.contrib import admin
from .models import MenuItem, Order, OrderItem, Delivery, Payment

class CoffeeMenu(admin.ModelAdmin):    
    list_display = ('name', 'category', 'price')
    search_fields = ('name',)
    list_filter = ('category',)
    ordering = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price', 'created_at')
    search_fields = ('id', 'user__username')
    list_filter = ('status', 'created_at')
    ordering = ('created_at',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity')
    search_fields = ('order__id', 'menu_item__name')
    ordering = ('order',)

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'estimated_delivery')
    search_fields = ('order__id',)
    list_filter = ('status',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'method', 'status', 'transaction_id')
    search_fields = ('order__id', 'transaction_id')
    list_filter = ('method', 'status')

admin.site.register(MenuItem, CoffeeMenu)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Payment, PaymentAdmin)
