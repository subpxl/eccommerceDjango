import datetime
from django.shortcuts import render,redirect
from  django.http import  HttpResponse,JsonResponse
from accounts.models import User
from .forms import OrderForm
from  .models import  Order,Payment
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
# Create your views here.
def order_view(request):
    return  HttpResponse('order page')

def place_order(request ):
    if request.method=="POST":        
        form = OrderForm(request.POST or None)
        
        if form.is_valid():
            amount =form.instance.grand_total
            name =form.instance.first_name 
            order = form.save()

            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d") #20210305

            order_number = current_date + str(order.id)
            order.order_number = order_number
            order.save()
            data = { "amount": amount *100, "currency": "INR", "receipt": order_number }
            payment_order = razorpay_client.order.create(data=data)

            payment = Payment.objects.create(user= request.user, name=name, amount=amount * 100, provider_order_id=payment_order["id"])
            payment.save()

            # get cart Items
            cart_items = CartItem.objects.filter(user=request.user)
            return render(request,'orders/payments.html',{
                "callback_url": "http://" + "localhost:8000" + "/order/razorpay/callback/",
                "razorpay_key":settings.RAZOR_KEY_ID,
                "payment": payment,
                'order':order,
                "cart_items":cart_items,
            },)    
        else:
            return JsonResponse(form.errors)

    else:
        return render(request,'order_test.html',{})



def payments(request):
    pass


def order_complete(request):
    pass


# string sample
#  {'razorpay_payment_id': 'pay_KEVyNPROq70qBk', 'razorpay_order_id': 'order_KEVxpxCjySmqOf', 'razorpay_signature': '214cf81efc184cd7cb3836c831df5fd5d30b18b796b4db1254875df6ad226413'}
@csrf_exempt
def razorpay_callback(request):

    if request.method =="POST":
            data = request.POST
            myDict = data.dict()
            
            print("###########################")
            print('the data is ',myDict)

            print("###########################")

            if 'razorpay_signature' not in myDict:
                return render(request, "callback.html", context={"status": myDict})

            else:
            
                is_success = razorpay_client.utility.verify_payment_signature(myDict)

                if is_success:

                    payment = Payment.objects.get(provider_order_id=myDict['razorpay_order_id'])
                    payment.payment_id =myDict['razorpay_payment_id']
                    payment.signature_id=myDict['razorpay_signature']
                    payment.status = "Success"
                    payment.save()

                    order = Order.objects.get(payment=payment)
                    order.status="Processing"
                    order.save()

                    return render(request, "callback.html", context={"status": is_success,'myDict':myDict})
                else:
                    return render(request, "callback.html", context={"status": is_success})

