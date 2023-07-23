from django.shortcuts import render, redirect, HttpResponseRedirect
from django.db import transaction

from users.models import Farmer
from .models import (Produce, Unit,  Purchase_produce, Produce_Ship_from_farm, Received_products, Warehouse, Stock)
from users.models import Employee, Transporter
from datetime import datetime


@transaction.atomic
def create_purchase_produce(request, id):
    user = request.user
    farmer = Farmer.objects.get(user_id=id)#.first()
    produces = Produce.objects.all()
    units = Unit.objects.all()

    if request.POST:
        buyer = Employee.objects.filter(user_id=user.user_id).first()
        produce_resp = request.POST["produce"]
        produce = Produce.objects.filter(produce_id=produce_resp).first()
        unit_resp = request.POST["unit"]
        unit = Unit.objects.filter(unit_id=unit_resp).first()
        quantity = request.POST["quantity"]
        total_weight = request.POST["total_weight"]
        total_price = request.POST["total_price"]   
        # date_bought = request.POST.get("date_bought") 
        # formatted_date = datetime.strptime(date_bought, '%Y-%m-%d')
        purchase = Purchase_produce( produce = produce ,unit =unit, quantity=quantity, buyer=buyer,
                                    total_weight = total_weight, total_price=total_price , farmer=farmer)
        purchase.save()
        
    context={
      
        "farmer": farmer,
        "produces": produces,
        "units" : units
    }
    return render(request, 'cms/create_purchase_produce.html', context)


def list_farmer_purchase_produce(request, id):
    '''
    list purchase orders of a specific farmer
    '''
    purchased_produces = Purchase_produce.objects.filter(farmer = id, is_deleted =False )
    print(purchased_produces)
    context ={"purchased_produces": purchased_produces}
    return render(request, 'cms/list_farmer_purchase_produce.html', context)


@transaction.atomic
def update_purchase_produce(request, id):
    all_produce = Produce.objects.all()
    units = Unit.objects.all()
    purchased_produce = Purchase_produce.objects.filter(purchase_produce_id=id ).first()
    context ={
        "all_produce": all_produce,
        "purchased_produce": purchased_produce,
        "units" : units
        }
    
    if request.POST:
        
        purchased_produce = Purchase_produce.objects.filter(purchase_produce_id=id ).first()
        produce_resp = request.POST.get("produce")
        purchased_produce.produce = Produce.objects.filter(produce_id=produce_resp).first()
        unit_resp = request.POST.get("unit")
        purchased_produce.unit = Unit.objects.filter(unit_id=unit_resp).first()
        purchased_produce.quantity = request.POST["quantity"]
        purchased_produce.total_weight = request.POST["total_weight"]
        purchased_produce.total_price = request.POST["total_price"]   
        purchased_produce.save()

    return render(request, 'cms/update_purchase_produce.html', context)


def delete_purchase_produce(request, id):
    if request.POST:
        purchase_product = Purchase_produce.objects.filter(purchase_produce_id=id ).first()
        print(purchase_product)
        purchase_product.is_deleted =True
        print(purchase_product)
        purchase_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



#Shipping_from_farm

def create_produce_ship_from_farm(request):
    produces = Produce.objects.all()
    units = Unit.objects.all()
    transporters = Transporter.objects.filter(is_active=True)

    if request.POST:
        user = request.user
        buyer = Employee.objects.filter(user_id=user.user_id).first()
        produce_resp = request.POST["produce"]
        produce = Produce.objects.filter(produce_id=produce_resp).first()
        unit_resp = request.POST["unit"]
        unit = Unit.objects.filter(unit_id=unit_resp).first()
        transporter_resp = request.POST["transporter"]
        transporter = Transporter.objects.filter(user_id=transporter_resp).first()
        quantity = request.POST["quantity"]
        driver_phone = request.POST["driver_phone"]
        total_produce_cost = request.POST["total_produce_cost"]
        shipping_cost = request.POST["shipping_cost"]

        produce_shipped = Produce_Ship_from_farm( produce=produce, unit=unit, quantity=quantity, transporter=transporter, driver_phone=driver_phone, 
                            total_produce_cost =total_produce_cost, shipping_cost=shipping_cost, buyer=buyer )
        produce_shipped.save()

    context = {
        "produces": produces,
        "units": units,
        "transporters": transporters
    }

    
    return render(request, 'cms/create_produce_ship_from_farm.html', context)


def list_produce_ship_from_farm(request):
    '''
    list purchase orders of a specific farmer
    '''
    purchased_produces = Produce_Ship_from_farm.objects.filter( is_deleted =False )
    print(purchased_produces)
    context ={"purchased_produces": purchased_produces}
    return render(request, 'cms/list_produce_ship_from_farm.html', context)


def update_produce_ship_from_farm(request, id):
    produces = Produce.objects.all()
    units = Unit.objects.all()
    transporters = Transporter.objects.filter(is_active=True)
    shipment = Produce_Ship_from_farm.objects.filter(shipment_id = id, is_deleted=False).first()

    if request.POST:
        user = request.user
        
        shipped_produce = Produce_Ship_from_farm.objects.filter(shipment_id=id ).first()
        shipped_produce.buyer = Employee.objects.filter(user_id=user.user_id).first()
        produce_resp = request.POST.get("produce")
        shipped_produce.produce = Produce.objects.filter(produce_id=produce_resp).first()
        unit_resp = request.POST.get("unit")
        shipped_produce.unit = Unit.objects.filter(unit_id=unit_resp).first()
        shipped_produce.quantity = request.POST["quantity"]
        transporter_resp = request.POST.get("transporter")
        shipped_produce.transporter = Transporter.objects.filter(user_id=transporter_resp).first()
        shipped_produce.driver_phone = request.POST["driver_phone"]
        shipped_produce.total_produce_cost = request.POST["total_produce_cost"]
        shipped_produce.shipping_cost = request.POST["shipping_cost"]  
        shipped_produce.save()
    
        return redirect('cms:list_produce_ship_from_farm')


    context = {
        "produces": produces,
        "units": units,
        "transporters": transporters,
        "shipment": shipment
    }

    
    return render(request, 'cms/update_produce_ship_from_farm.html', context)


def delete_produce_ship_from_farm(request, id):
    if request.POST:
        purchase_product = Produce_Ship_from_farm.objects.filter(shipment_id=id ).first()
        purchase_product.is_deleted =True
     
        purchase_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Received_products
def create_received_products(request):
    produces = Produce.objects.all()
    units = Unit.objects.all()
    warehouses = Warehouse.objects.all()
    transporters = Transporter.objects.filter(is_active=True)

    if request.POST:
        print(request.POST["warehouse"])
        user = request.user
        received_by = Employee.objects.filter(user_id=user.user_id).first()
        produce_resp = request.POST["produce"]
        produce = Produce.objects.filter(produce_id=produce_resp).first()
        unit_resp = request.POST["unit"]
        unit = Unit.objects.filter(unit_id=unit_resp).first()
        transporter_resp = request.POST["transporter"]
        transporter = Transporter.objects.filter(user_id=transporter_resp).first()
        warehouse_resp = request.POST["warehouse"]
        warehouse = Warehouse.objects.filter(warehouse_id=warehouse_resp).first() 
        quantity = request.POST["quantity"]

        received_products = Received_products(received_by=received_by,  produce=produce, unit=unit,transporter=transporter , 
                                              warehouse=warehouse, quantity=quantity)
        
        received_products.save()

    context = {
        "produces": produces,
        "units": units,
        "warehouses": warehouses,
        "transporters": transporters
    }
    
    return render(request, 'cms/create_received_products.html', context)



def list_received_products(request):
    '''
    list purchase orders of a specific farmer
    '''
    produces = Received_products.objects.filter( is_deleted =False )
    context ={"produces": produces}
    return render(request, 'cms/list_received_products.html', context)


def update_received_products(request, id):
    '''
    Updates products received on the warehouse
    '''
    produces = Produce.objects.all()
    units = Unit.objects.all()
    transporters = Transporter.objects.filter(is_active=True)
    warehouses = Warehouse.objects.all()
    received_products = Received_products.objects.filter(received_product_id = id, is_deleted=False).first()

    if request.POST:
        user = request.user
        
        received_produce = Received_products.objects.filter(received_product_id=id ).first()
        received_produce.received_by = Employee.objects.filter(user_id=user.user_id).first()
        produce_resp = request.POST.get("produce")
        received_produce.produce = Produce.objects.filter(produce_id=produce_resp).first()
        unit_resp = request.POST.get("unit")
        received_produce.unit = Unit.objects.filter(unit_id=unit_resp).first()
        received_produce.quantity = request.POST["quantity"]
        transporter_resp = request.POST.get("transporter")
        received_produce.transporter = Transporter.objects.filter(user_id=transporter_resp).first()
        warehouse_resp = request.POST.get("warehouse")
        received_produce.warehouse = Warehouse.objects.filter(warehouse_id=warehouse_resp).first()
        received_produce.save()

        return redirect('cms:list_received_products')


    context = {
        "produces": produces,
        "units": units,
        "transporters": transporters,
        "received_products": received_products,
        "warehouses" : warehouses
    }

    
    return render(request, 'cms/update_received_products.html', context)


def delete_received_products(request, id):
    if request.POST:
        purchase_product = Received_products.objects.filter(received_product_id=id ).first()
        purchase_product.is_deleted =True
        purchase_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# create stock on differnt warehouses

def create_stock(request):
    produces = Produce.objects.all()
    units = Unit.objects.all()
    warehouses = Warehouse.objects.all()


    if request.POST:
        user = request.user
        created_by = Employee.objects.filter(user_id=user.user_id).first()
        produce_resp = request.POST["produce"]
        produce = Produce.objects.filter(produce_id=produce_resp).first()
        unit_resp = request.POST["unit"]
        unit = Unit.objects.filter(unit_id=unit_resp).first()
        warehouse_resp = request.POST["warehouse"]
        warehouse = Warehouse.objects.filter(warehouse_id=warehouse_resp).first() 
        quantity = request.POST["quantity"]

        stocked_products = Stock(created_by=created_by,  produce=produce, unit=unit,
                                              warehouse=warehouse, quantity=quantity)      
        stocked_products.save()

    context = {
        "produces": produces,
        "units": units,
        "warehouses": warehouses
    }
    
    return render(request, 'cms/create_stock.html', context)


def list_stock(request):
    stocks = Stock.objects.filter( is_deleted =False )
    context ={"stocks": stocks}
    return render(request, 'cms/list_stock.html', context)


def update_stock(request, id):
    '''
    Updates products received on the warehouse
    '''
    produces = Produce.objects.all()
    units = Unit.objects.all()
    warehouses = Warehouse.objects.all()
    stock = Stock.objects.filter(stock_id = id, is_deleted=False).first()

    if request.POST:
        user = request.user
        warehouse_stock = Stock.objects.filter(stock_id=id ).first()
        warehouse_stock.created_by = Employee.objects.filter(user_id=user.user_id).first()
        produce_resp = request.POST.get("produce")
        warehouse_stock.produce = Produce.objects.filter(produce_id=produce_resp).first()
        unit_resp = request.POST.get("unit")
        warehouse_stock.unit = Unit.objects.filter(unit_id=unit_resp).first()
        warehouse_stock.quantity = request.POST["quantity"]
        warehouse_resp = request.POST.get("warehouse")
        warehouse_stock.warehouse = Warehouse.objects.filter(warehouse_id=warehouse_resp).first()
        warehouse_stock.save()

        return redirect('cms:list_stock')
    
    context = {
        "produces": produces,
        "units": units,
        "stock": stock,
        "warehouses" : warehouses
    }

    
    return render(request, 'cms/update_stock.html', context)


def delete_stock(request, id):
    if request.POST:
        stock = Stock.objects.filter(stock_id=id ).first()
        stock.is_deleted =True
        stock.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
