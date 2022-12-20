from django.shortcuts import render,redirect
from .models import Seller,Category,Catalogue,Product,StoreFront,Links,UserOtp
from django.http import HttpResponse
# Create your views here.
from .forms import AddressForm
from accounts.models import User
from django.contrib import messages
from orders.models import Order,OrderProduct,Payment
import random
import string
from orders.forms import OrderForm
N=8




def login(request):

    if request.method=='POST' :
        mobileNumber = request.POST.get("mobileNumber", "")
        # otp =  random.randint(1000000,9999999)
        otp ='rrrr'
        userOtp = UserOtp(mobileNumber='111111',otp='ooooo' )
        respo=  userOtp.save()
        return HttpResponse(respo)
        context = {
            'mobileNumber':mobileNumber,
        }
        return  render(request,'seller/login.html',context)
    else:
        return render(request,'seller/login.html')


def verifyotp(request):

    if request.method=='POST' :
        mobileNumber = request.POST.get("mobileNumber", "")

        otp = request.POST.get("otp", "")

        password = ''.join(random.choices(string.ascii_lowercase +
                                          string.digits, k=N))
        user = User.objects.create_user(username=mobileNumber, password=password, email='trst@test.com')
        response = user.save()
        context = {
            'slug':""
        }
        return render(request,'seller/verifyotp.html',context)


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products':products
    }
    return render(request,'seller/home.html',context)

def seller_page(request,slug):
    # seller = StoreFront.objects.get(slug=slug)
    seller = Seller.objects.get(slug=slug)

    links = Links.objects.get(seller=seller)
    products = Product.objects.filter(seller=seller)

    context ={       
        'seller':seller,
        'products':products,
        'links':links
    }

    return render(request,'seller/seller_page.html',context)

def all_sellers(request):
    sellers = Seller.objects.all()
    context = {
        'sellers':sellers
    }
    # return HttpResponse('t')
    return render(request,'seller/seller_list.html',context)

def store(request):
    lengthy = [1,2,3,4,5,6]
    context = {
        'lengthy':lengthy
    }
    return render(request,'seller/store.html',context)



def product_page(request,slug):
    product = Product.objects.get(slug=slug)
    seller_products = Product.objects.filter(seller=product.seller)
    context = {
        'product':product,
        'seller_products':seller_products,
        'slug':slug
    }
    return render(request,'seller/product.html',context)

def category_page(request,slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category.id)
    context = {
        'products':products,
        'category':category
    }
    return render(request,'seller/category_page.html',context)



def cart(request):
    context = {
        'slug':""
    }
    return render(request,'seller/cart.html',context)




def checkout(request):
    form = OrderForm()
    context = {
        "form":form,
    }

    if request.method=="POST":
        
        # todo add payment option in checkout
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review')
        else:
            context['errors']=form.errors
            return render(request,'seller/checkout.html',context)
    return render(request,'seller/checkout.html',context)



def order(request):
    context = {
        'slug':""
    }
    return render(request,'seller/order.html',context)

def order_details(request,slug):
    # order = Order.objects.get(slug=slug)
    context = {
        'order':"order"
    }
    return render(request,'seller/order-view.html',context)

def myaccount(request):
    context = {
        'slug':""
    }
    return render(request,'seller/my-account.html',context)

# account and auth




def register(request):
    context = {
        'slug':""
    }
    return render(request,'seller/register.html',context)


def registerAsVendor(request):
    pass


def search(requst):
    context = {
        '':""
    }
    return  render(requst,'seller/search.html',context)

def track_order(requst):
    context = {
        '':""
    }
    return  render(requst,'seller/track_order.html',context)


def deals(requst):
    context = {
        '':""
    }
    return  render(requst,'seller/deals.html',context)



def orderstatus(request):
    context = {
        '':""
    }
    return render(request,'seller/order_status.html',context)


def review(request):
    
    context = {
        '':""
    }
    return render(request,'seller/order_review.html',context)