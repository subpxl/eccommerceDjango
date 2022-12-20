from django.contrib import admin
from .models import Cart,CartItem,Tax
# Register your models here.

class TaxAdmin(admin.ModelAdmin):
    list_display: ('tax_type',)

    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'tax'
        verbose_name_plural = 'taxes'

# admin.site.register(Cart)
# admin.site.register(CartItem)
# admin.site.register(Tax,TaxAdmin)