from django.shortcuts import render


from  seller.models import  Product
# Create your views here.

def home(request):
    product_list = Product.objects.all().filter(is_available=True)
    context = {
        'product_list':product_list
    }
    return render(request,'home.html',context)