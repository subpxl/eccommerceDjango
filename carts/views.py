import re
from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product
from  django.http import HttpResponse
from .models import Cart,CartItem
# Create your views here.

from django.contrib.auth.decorators import login_required


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart= request.session.create()
    return cart





def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)

    current_user = request.user
    if current_user.is_authenticated:
        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, user=current_user)
            item = CartItem.objects.create(product=product, quantity=1, user=current_user)


    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request),
        )
        print('cart creaeted')
    cart.save()

    try:
        cart_item=CartItem.objects.get(product=product, cart=cart)

        if cart_item != None:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            cart_item.quantity +=1
            cart_item.save()
        else:
            cart_item=CartItem.objects.create(product=product,quantity =1, cart=cart)
            cart_item.save()

    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0

    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart_id = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart_id, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except :
        pass 

    context = {
        'tax':tax,
        'grand_total':grand_total,
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)

    # return  HttpResponse(quantity)



def remove_cart(request,product_id):
    
    if request.user.is_authenticated:
        product=get_object_or_404(Product,id=product_id)
        cart_item = CartItem.objects.get(product=product,user=request.user)
    
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        product=get_object_or_404(Product,id=product_id)
        cart_item = CartItem.objects.get(product=product,cart=cart)
        
        
    if cart_item.quantity>1:
        cart_item.quantity-=1
        cart_item.save()

    else:
        cart_item.delete()

    return  redirect('cart')




@login_required
def checkout(request):

    try:
        tax = 0
        grand_total =0
        total =0
        quantity = 0

        # cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(user=request.user,is_active=True)
        for cart_item in  cart_items:
            total +=(cart_item.product.price *cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2*total)/100
        grand_total = total+tax
    
            # implememt razorpay

    except:
        pass

    context ={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total
    }
    return  render(request,'checkout.html',context) 