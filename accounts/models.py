from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.TextField(max_length=20, blank=False)
    is_verified = models.BooleanField(default=False)
    email = models.EmailField( blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("staff_list")

    def __str__(self) -> str:
        return f'{self.username}'



class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name}'


class Buyer(models.Model):
    name = models.CharField(max_length=100,default='')
    is_active = models.BooleanField(default=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.name}'