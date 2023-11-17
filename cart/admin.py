from django.contrib import admin
from .models import Cart
class CartAdmin(admin.ModelAdmin):
    list_filter = ( 'terminated',)
    search_fields = ('user',)

admin.site.register(Cart, CartAdmin)