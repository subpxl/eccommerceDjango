from re import T
from django.db import models
from  seller.models import Product
from  accounts.models import  User
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    is_active =models.BooleanField(default=True)

    def sub_total(self):
        return  self.product.price *self.quantity

    def __str__(self):
        return f'{self.product}'


class Tax(models.Model):
    tax_type = models.CharField(max_length=50,unique=True)
    tax_percentage = models.DecimalField(decimal_places=2,max_digits=4,verbose_name='Tax Percentage')
    is_active = models.BooleanField(default=True)

    def __str__(self) :
        return f'{self.tax_type}'