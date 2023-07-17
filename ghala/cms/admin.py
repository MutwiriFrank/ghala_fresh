from django.contrib import admin
from . models import (Produce, Product_services, Purchase_produce, Received_products, 
                      Returned_produce, Repackaged_produce_to_services, Gateway, Shipping_from_farm,
                    Sales, Stock, Warehouse, Repackaged_produce,Unit, Order_item, Opening_closing_stock, 
                    Order, Order_payment)

# Register your models here.
admin.site.register(Produce)
admin.site.register(Product_services)
admin.site.register(Purchase_produce)
admin.site.register(Received_products)
admin.site.register(Returned_produce)
admin.site.register(Repackaged_produce_to_services)
admin.site.register(Gateway)
admin.site.register(Shipping_from_farm)
admin.site.register(Sales)
admin.site.register(Stock)
admin.site.register(Warehouse)
admin.site.register(Repackaged_produce)
admin.site.register(Unit)
admin.site.register(Order_item)
admin.site.register(Opening_closing_stock)
admin.site.register(Order)
admin.site.register(Order_payment)