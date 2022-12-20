from django.contrib import admin

# Register your models here.
from .models import  StoreFront

class StoreFrontAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(StoreFront,StoreFrontAdmin)