from django.contrib import admin
from .models import Product , TestDateAndTime

class ProductAdmin (admin.ModelAdmin) :
    list_display = ['name','price','category','active']
    list_display_links = ['name']
    list_editable = ['price','active']
    search_fields = ['name']
    list_filter = ['category','price']
    #fields = ['name','price']

# Register your models here
admin.site.register (Product,ProductAdmin)
#admin.site.register (TestDateAndTime)