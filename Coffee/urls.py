from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, OrderViewSet, DeliveryViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'delivery', DeliveryViewSet)
router.register(r'payment', PaymentViewSet)
urlpatterns = [
    path('',views.home),
    path('', include(router.urls)),  # Registers API routes
]

