from  django.urls import  path
from django.views.generic import TemplateView 
from  .views import (
        home,
        all_sellers,seller_page,
        product_page,category_page,
        cart,checkout,myaccount,
        login,verifyotp,register,registerAsVendor,
        order,order_details,
        search,track_order,deals,
        review,orderstatus
)
urlpatterns =[
 
    path('product/<slug:slug>/',product_page,name='product'),
    path('category/<slug:slug>/',category_page,name='category'),
    
    path('cart/',cart,name='cart'),
    path('checkout/',checkout,name='checkout'),
    path('my-account/',myaccount,name='myaccount'),
    
    path('order/<slug:slug>/',order_details,name='order_details'),
    path('order/',order,name='order'),
    path('review/', review, name='review'),
    path('orderstatus/', orderstatus, name='orderstatus'),

    path('login/',login,name='login'),
    path('verifyotp/',verifyotp,name='verifyotp'),
    path('register/',register,name='register'),
    path('register-as-vendor/', registerAsVendor, name='registerAsVendor'),

    path('contact/',TemplateView.as_view(template_name='seller/static/contact-us.html'),name='contact'),
    path('about/',TemplateView.as_view(template_name='seller/static/about-us.html'),name='about'),

    path('search/', search, name='search'),
    path('track-order/', track_order, name='track_order'),
    path('deals/', deals, name='deals'),

    path('sellers/',all_sellers,name='all_sellers'),
    path('<slug:slug>/',seller_page,name='seller'),


    # seller frontpage page
    path('',home,name='home'),

]