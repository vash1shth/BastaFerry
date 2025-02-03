from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price')
    search_fields = ('name', 'color')

admin.site.register(Product, ProductAdmin)

