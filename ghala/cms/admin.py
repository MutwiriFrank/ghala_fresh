from django.contrib import admin
from . models import (Produce, Product_services, Purchase_produce, Received_products, 
                      Returned_produce, Shipped_produce_to_services, Gateway, Produce_Ship_from_farm,
                    Sales, Stock, Warehouse,Unit, Order_item, 
                    Order, Order_payment, Opening_closing_stock)

# Register your models here.
admin.site.register(Produce)
admin.site.register(Product_services)
admin.site.register(Purchase_produce)
admin.site.register(Received_products)
admin.site.register(Returned_produce)
admin.site.register(Shipped_produce_to_services)
admin.site.register(Gateway)
admin.site.register(Produce_Ship_from_farm)
admin.site.register(Sales)
admin.site.register(Stock)
admin.site.register(Warehouse)
admin.site.register(Unit)
admin.site.register(Order_item)
admin.site.register(Opening_closing_stock)
admin.site.register(Order)
admin.site.register(Order_payment)