from django.urls import path
from .views import (create_purchase_produce, list_farmer_purchase_produce, update_purchase_produce , delete_purchase_produce
    , list_produce_ship_from_farm, create_produce_ship_from_farm, update_produce_ship_from_farm, delete_produce_ship_from_farm, 
    create_received_products,  list_received_products, delete_received_products, update_received_products,
    create_stock, list_stock, update_stock, delete_stock
    )

app_name = 'cms'

urlpatterns = [
    path('purchase-produce/create/<str:id>/', create_purchase_produce, name="create_purchase_produce"),
    path('purchase-produce/list/<str:id>/', list_farmer_purchase_produce, name="list_farmer_purchase_produce"),
    path('purchase-produce/update/<str:id>/', update_purchase_produce, name="update_purchase_produce"),
    path('purchase-produce/delete/<str:id>/', delete_purchase_produce, name="delete_purchase_produce"),

    path('ship-from-farm/create', create_produce_ship_from_farm, name="create_produce_ship_from_farm"),
    path('ship-from-farm/list', list_produce_ship_from_farm, name="list_produce_ship_from_farm"),
    path('ship-from-farm/update/<str:id>/', update_produce_ship_from_farm, name="update_produce_ship_from_farm"),
    path('ship-from-farm/delete/<str:id>/', delete_produce_ship_from_farm, name="delete_produce_ship_from_farm"),

    path('received-products/create', create_received_products, name="create_received_products"),
    path('received-products/list', list_received_products, name="list_received_products"),
    path('received-products/update/<str:id>/', update_received_products, name="update_received_products"),
    path('received-products/delete/<str:id>/', delete_received_products, name="delete_received_products"),

    path('stock/create', create_stock, name="create_stock"),
    path('stock/list', list_stock, name="list_stock"),
    path('stock/update/<str:id>/', update_stock, name="update_stock"),
    path('stock/delete/<str:id>/', delete_stock, name="delete_stock")
 
]
