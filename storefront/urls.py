from django.urls import path
from .views import storefront,home
urlpatterns =[
    path('',home,name='home'),
    path('<slug:slug>/',storefront,name='storefront')
]