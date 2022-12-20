from django.urls import path
from .views import  order_view,place_order,razorpay_callback,payments,order_complete
from .razorpay_view import homepage,paymenthandler

urlpatterns = [
    path('place_order/', place_order, name='place_order'),
    path('payments/', payments, name='payments'),
    path('order_complete/', order_complete, name='order_complete'),

       path('ordertest', homepage, name='homepage'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
    path('razorpay/callback/', razorpay_callback, name='razorpay_callback'),
 
]