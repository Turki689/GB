from django.contrib import admin

from .models import Item, Order


class ItemInline(admin.TabularInline):
    model = Item
    fields = ['product', 'quantity', 'price']
    readonly_fields = ['price', 'product', 'quantity']
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone_number', 'country', 'city',
                    'zip_code', 'state', 'username']
    readonly_fields = ['id', 'email', 'phone_number', 'country', 'city',
                       'zip_code', 'state', 'username']
    inlines = [ItemInline]


admin.site.register(Order, OrderAdmin)
