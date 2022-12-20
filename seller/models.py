from django.db import models
from django.utils.text import slugify
from  django.db.models.signals import  post_save,pre_save
from  django.dispatch import receiver

from accounts.models import User



class UserOtp(models.Model):
    mobileNumber =models.CharField(max_length=12,null=False)
    otp=models.CharField(max_length=20,null=False)

    def __abs__(self):
        return  f'{self.mobileNumber}'

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company =models.CharField(max_length=100)
    name =models.CharField(max_length=100)
    address_line1 =models.CharField(max_length=100)
    address_line2 =models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    phone =models.CharField(max_length=100)
    email=models.CharField(max_length=100)

    def __str__(self):
        return  f'{self.phone}'
class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    picode = models.CharField(max_length=100)

    logo=models.ImageField(upload_to='photos/logo')
    image=models.ImageField(upload_to='photos/seller/')
    slug=models.SlugField(max_length=100,unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Seller, self).save(*args, **kwargs)

    def __str__(self) :
        return f'{self.name}'


class StoreFront(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    logo=models.ImageField(upload_to='photos/logo')
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    picode = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50,blank=False)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photos/Storefront')
    created_date =models.DateTimeField(auto_now=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50,blank=False)
    image=models.ImageField(upload_to='photos/Category')
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)

    created_date =models.DateTimeField(auto_now=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=False)
    image=models.ImageField(upload_to='photos/Product')
    seller =models.ForeignKey(Seller,on_delete=models.CASCADE) 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()
    sale_price = models.PositiveBigIntegerField()
    sku=models.CharField(max_length=100,null=True,blank=True)
    video_link = models.CharField(max_length=250,null=True,blank=True)
    short_description = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    created_date =models.DateTimeField(auto_now=True)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Catalogue(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=False)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.name}'





class Links(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    facebook =models.CharField( max_length=254, blank=True, null=True)
    instagram =models.CharField( max_length=254, blank=True, null=True)
    youtube=models.CharField( max_length=254, blank=True, null=True)
    twitter =models.CharField( max_length=254, blank=True, null=True)
    whatsapp =models.CharField( max_length=254, blank=True, null=True)

    def __str__(self):
        return f"{self.id}-{self.seller}"


@receiver(post_save,sender=Seller)
def create_link(sender,instance,created,**kwargs):
    if created:
        Links.objects.create(seller=instance)


