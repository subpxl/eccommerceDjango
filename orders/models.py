from operator import mod
from pyexpat import model
from django.db import models
from accounts.models import   User
from seller.models import  Product, Address


class Payment(models.Model):
    STATUS = (
            ('Success' , "Success"),
            ('Failure' , "Failure"),
            ('Pending' , "Pending"),)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField( max_length=254, blank=False, null=False)
    payment_method = models.CharField(max_length=100,null=True,blank=True)
    amount = models.FloatField( null=False, blank=False)
    status = models.CharField( default="Pending",max_length=254,blank=False,null=False,)
    provider_order_id = models.CharField( max_length=40, null=False, blank=False)
    payment_id = models.CharField(max_length=36, null=False, blank=False)
    signature_id = models.CharField(max_length=128, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"



class Order(models.Model):
    STATUS = (
        ('New','New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
        ('Processing','Processing'), )

    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name =models.CharField(max_length=100)
    # company =models.CharField(max_length=100)
    address_line1 =models.CharField(max_length=100)
    address_line2 =models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    phone =models.CharField(max_length=100)
    email=models.CharField(max_length=100,blank=True,null=True)
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,blank=True,null=True)  
    order_number=models.CharField(max_length=100,blank=True,null=True)
    total=models.FloatField()
    tax=models.FloatField()
    grand_total=models.FloatField()
    status=models.CharField(max_length=100,choices=STATUS,default='New',blank=True,null=True)
    # order_note=models.CharField(max_length=100,blank=True,null=True)

    is_ordered=models.BooleanField(default=False,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'

    def get_full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'


class OrderProduct(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment,on_delete=models.SET_NULL,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    # variation
    color=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    quantity=models.IntegerField()
    product_price=models.FloatField()
    is_ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name


