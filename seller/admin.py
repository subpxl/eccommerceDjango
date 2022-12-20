from .models import Product
from django.contrib import admin
from .models import Seller,StoreFront,Links,Address,UserOtp

# Register your models here.

class SellerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Seller,SellerAdmin)

from .models import Catalogue,Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','slug')


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','slug','price','sale_price','category')


class CatalogueAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','slug')


class StoreFrontAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','slug',)


class OrderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','slug',)





admin.site.register(Links)
admin.site.register(UserOtp)
admin.site.register(StoreFront,StoreFrontAdmin)
admin.site.register(Address)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Catalogue,CatalogueAdmin)

