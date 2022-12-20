from django.db import models
from accounts.models import Seller
# Create your models here.


class StoreFront(models.Model):
    CHOICES = (
        ('business','business'),
        ('shop','shop'),
    )

    THEMES = (
        ('theme1','theme1'),
        ('theme2','theme2'),
        ('theme3','theme3'),
        ('theme4','theme4'),
        ('theme5','theme5'),
        ('theme6','theme6'),
        ('theme7','theme7'),
    )
    
    REGISTRAR = (
     ('godaddy.com','godaddy.com'),
     ('namecheap.com','namecheap.com'),
     ('bigrock.in','bigrock.in'),
    )

    domain = models.CharField(max_length=100,null=True)
    registrar = models.CharField(max_length=100,choices=REGISTRAR,null=True)
    is_active = models.BooleanField(default=True)

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    # short_description =  models.CharField(max_length=100)
    aboutUsPhoto = models.ImageField(upload_to='seller/storefront/')
    logo = models.ImageField(upload_to='seller/storefront/')
    theme = models.CharField(max_length=100,choices=THEMES,default='theme1')
    slug=models.SlugField(max_length=100,unique=True)
    type = models.CharField(max_length=100 , choices=CHOICES,default='shop')
    def __str__(self) :
        return f'{self.name}'









