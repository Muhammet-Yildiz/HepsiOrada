from django.contrib import admin

from .models import Order,OrderItem,ShippingAddres,Customer


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddres)