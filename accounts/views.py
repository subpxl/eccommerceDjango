from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse

from carts.models import CartItem, Cart
from carts.views import _cart_id
from .forms import UserForm

# Create your views here.
from .models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def registerUser(request):
    if request.method=="POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']

            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request,'your account has been registered successfully     ')
            return redirect('registerUser')

        else:
            print('form is invalid')
            print(form.errors)

    else:
        form = UserForm()
        context ={
            'form':form,
            
        }
        return render(request,'accounts/registerUser.html',context)



# todo refactor all functions from user user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        print(user)

        if user is not None:
            try:
                            
                print('before the cart id is ',_cart_id(request))
                cart = Cart.objects.get(cart_id=_cart_id(request))
                
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)

                    for item in cart_item:
                        print('cate item is',cart_item )
                        item.user = user
                        item.save()
            except:
                pass

            login(request, user)


            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                

            except:
                pass
            return redirect('store')


        else:
            redirect('login')
            messages.info(request, "username or password is incorrect")

    print('before the cart id is ',_cart_id(request))
    return render(request, 'accounts/login.html')



@login_required(login_url = 'login')
def logoutPage(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')


def dashboard(request):
    return HttpResponse("trtr")
    # return  render(request,'accounts/dashboard.html',{})