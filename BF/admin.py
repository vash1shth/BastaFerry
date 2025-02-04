from django.contrib import admin
from .models import Product, UserProfile, Address, PastOrder

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price')
    search_fields = ('name', 'color')

admin.site.register(Product, ProductAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'gender', 'date_of_birth')
    search_fields = ('user__username', 'phone_number', 'gender')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_line1', 'city', 'state', 'country')
    search_fields = ('user__username', 'city', 'state', 'country')

class PastOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'order_date', 'quantity', 'total_price')
    search_fields = ('user__username', 'product__name', 'order_date')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(PastOrder, PastOrderAdmin)

