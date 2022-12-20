from  django.urls import  path
from .views import cart,add_cart,remove_cart,checkout
urlpatterns = [
    path('',cart,name='cart'),
    path('add_cart/<int:product_id>/', add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/', remove_cart, name='remove_cart'),
    path('checkout/',checkout,name='checkout'),
]