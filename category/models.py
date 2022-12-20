from django.db import models
from  django.shortcuts import reverse

class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50,unique=True)
    description=models.CharField(max_length=200,blank=True)
    cat_image=models.ImageField(upload_to='photos/category',blank=True)

    def __str__(self):
        return  self.category_name

    def get_url(self):
        return  reverse('products_by_category' ,args=[self.slug])

    class Meta:
        verbose_name='category'
        verbose_name_plural = 'categories'