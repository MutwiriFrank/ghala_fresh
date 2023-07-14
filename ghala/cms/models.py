from django.db import models
from users.models import (Location, Farmer, Vendor, Transporter, NewUser )

import uuid
# Create your models here.

PRODUCE_STORAGE_PERIOD = (                                                                          

    ("Less than a week" , "less than a week"),
    ("less than 2 weeks" , "less than 2 weeks"),
    ("less than a month" , "less than a month "),
    ("more than a month" , "more than a month")
)

class Unit (models.Model):
    unit_id = models.CharField(max_length=10, primary_key=True, blank=False, null=False )
    unit_name = models.CharField(max_length=100, unique=True,  blank=False, null=False, db_index=True)
    unit_description = models.ForeignKey(Location, db_column="location_id", on_delete=models.SET_NULL,
                                          null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL,
                                    related_name = 'unit_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='unit_updated_by', null=True, blank=True)

    class Meta:
        verbose_name = ("Units")
        verbose_name_plural = ("Units")

    def __str__(self):
        return self.unit_name


class Produce(models.Model):
    produce_id =  models.UUIDField(primary_key=True,  default=uuid.uuid4, editable=False)
    produce_name = models.CharField(max_length=100, unique=True, blank=False, null=False, db_index=True)
    produce_description = models.TextField( null=True, blank=True )
    source_location_1 = models.ForeignKey(Location,  related_name="produce_source_location_1", 
                                        on_delete=models.SET_NULL, null=True, blank=True)
    source_location_2 = models.ForeignKey(Location, related_name="produce_source_location_2", 
                                        on_delete=models.SET_NULL, null=True, blank=True)
    source_location_3 = models.ForeignKey(Location, related_name="produce_source_location_3",
                                        on_delete=models.SET_NULL, null=True, blank=True)
    storage_period = models.CharField(max_length=100, choices=PRODUCE_STORAGE_PERIOD , null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, related_name = 'produce_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, related_name='produce_updated_by', null=True, blank=True)

    def __str__(self) :
        return self.produce_name
    

class Purchase_produce(models.Model):
    farmer =  models.ForeignKey(Farmer, db_column="user_id",
        related_name='purchase_produce_farmer', on_delete=models.SET_NULL, null=True, blank=True)
    produce = models.ForeignKey(Produce, db_column="produce_id", 
        related_name='purchase_produce_produce', on_delete=models.SET_NULL, null=True, blank=True)
    unit = models.ForeignKey(Unit, db_column="unit_id",related_name='purchase_produce_unit', 
                            on_delete=models.SET_NULL,  null=True, blank=True)
    location = models.ForeignKey(Location, db_column="location_id", 
            related_name='purchase_produce_location', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.DecimalField(max_digits=9, decimal_places=3, null=False, blank=False)
    total_weight = models.DecimalField(max_digits=9, decimal_places=3, null=True, blank=True)
    total_price = models.DecimalField(max_digits=9, decimal_places=3, null=False, blank=False)
    date_bought = models.DateField(null=False, blank=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name = 'purchase_produce_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='purchase_produce_updated_by', null=True, blank=True)

    def __str__(self) :
        return self.produce + self.total_price +'  -  '  + self.date_bought
    
    class Meta:
        ordering = ['created_at']


class Shipment_from_farm(models.Model):
    shipment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transporter = models.ForeignKey(Transporter, related_name= 'shipment_from_farm_transporter', 
                                    on_delete=models.SET_NULL , null=True, blank=True)
    driver_phone = models.CharField(max_length=13, null=False, blank=False)
    loading_timestamp = models.DateTimeField(null=True, blank=True)
    departure_timestamp = models.DateTimeField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name = 'shipment_from_farm_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='shipment_from_farm_updated_by', null=True, blank=True)

    class Meta:
        indexes = (
            models.Index(fields=('driver_phone', 'departure_timestamp')),
        )
    def __str__(self) :
        return self.driver_phone+'  -  '  + self.departure_timestamp

class Repackaged_produce(models.Model):
    repackaged_produce_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, 
                                             db_index=True)
    produce = models.ForeignKey(Produce, db_column='produce_id', on_delete=models.RESTRICT,
                                 related_name = 'repackaged_produce_produce', null=False, blank=False)
    unit = models.ForeignKey(Unit, db_column='unit_id', on_delete=models.RESTRICT, 
                             related_name = 'repackaged_produce_unit', null=False, blank=False)
    unit_quantity = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    shipment_from_farm = models.ForeignKey(Shipment_from_farm, db_column='shipment_id', on_delete=models.RESTRICT,
                related_name = 'repackaged_produce_shipment_from_farm', null=False, blank=False)
    total_product_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    date_repacked = models.DateField(null=False, blank=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name = 'repackaged_produce_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='repackaged_produce_updated_by', null=True, blank=True)

    def __str__(self) :
        return self.produce+'  -  '  +self.unit+'  -  '  + self.unit_quantity+'  -  '  + self.date_repacked


class Product_services(models.Model):
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    service_name = models.CharField(max_length=100, null=False, blank=False)
    service_description = models.TextField(  null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                            related_name = 'product_services_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL,
                            related_name='product_services_updated_by', null=True, blank=True)

    def __str__(self) :
        return self.service_name


class Repackaged_produce_to_services(models.Model):
    product_to_service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    product_service = models.ForeignKey(Product_services, db_column='service_id', 
                                        on_delete=models.RESTRICT, null=False, blank=False)
    repackaged_produce = models.ForeignKey(Repackaged_produce, db_column='repackaged_produce_id', 
                                           on_delete=models.RESTRICT, null=False, blank=False)
    service_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                related_name = 'repackaged_produce_to_services_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                related_name='repackaged_produce_to_services_updated_by', null=True, blank=True)


class Warehouse(models.Model):
    warehouse_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, 
                                    db_index=True)
    warehouse_name = models.CharField(max_length=100, null=False, blank=False)
    warehouse_description = models.TextField(  null=False, blank=False)
    location = models.ForeignKey(Location, db_column="location_id", on_delete=models.SET_NULL,
                                  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL,
                                    related_name = 'warehouse_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='warehouse_updated_by', null=True, blank=True)

    def __str__(self) :
        return self.warehouse_name


class Received_products(models.Model):
    '''
    Produce received on the warehouse from farms
    '''
    received_products = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, 
                                         db_index=True)
    produce = models.ForeignKey(Produce, db_column='produce_id', on_delete=models.SET_NULL,
                                 related_name = 'received_products_produuce', null=True, blank=True)
    warehouse = models.ForeignKey(Warehouse, db_column='warehouse_id', on_delete=models.SET_NULL, 
                                  related_name = 'received_products_warehouse', null=True, blank=True)
    unit = models.ForeignKey(Unit, db_column='unit_id', on_delete=models.SET_NULL, 
                             related_name = 'received_products_unit', null=True, blank=True)
    unit_quantity = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    date_received = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name = 'received_products_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='received_products_updated_by', null=True, blank=True)


class Stock(models.Model):
    stock_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    warehouse = models.ForeignKey(Warehouse, db_column='warehouse_id', on_delete=models.SET_NULL, 
                                  related_name = 'stock_warehouse', null=True, blank=True)
    produce = models.ForeignKey(Produce, db_column='produce_id', on_delete=models.SET_NULL, 
                                related_name = 'stock_produuce', null=True, blank=True)
    unit = models.ForeignKey(Unit, db_column='unit_id', on_delete=models.SET_NULL, 
                             related_name = 'stock_unit', null=True, blank=True)
    unit_quantity = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    unit_price =  models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name = 'stock_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='stock_updated_by', null=True, blank=True)


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    vendor = models.ForeignKey(Vendor,  db_column='vendor_id', on_delete=models.SET_NULL, 
                               related_name = 'order_vendor', null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name = 'order_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='order_updated_by', null=True, blank=True)
    

class Order_item(models.Model):
    order_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order,  db_column='order_id', on_delete=models.SET_NULL, 
                               related_name = 'order_item_order', null=True, blank=True)
    produce = models.ForeignKey(Produce,  db_column='produce_id', on_delete=models.SET_NULL, 
                               related_name = 'order_produce', null=True, blank=True,  db_index=True)
    unit = models.ForeignKey(Unit, db_column='unit_id', on_delete=models.SET_NULL, 
                             related_name = 'order_item_unit', null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name = 'order_item_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='order_item_updated_by', null=True, blank=True)


class Gateway(models.Model):
    gateway_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, 
                                    db_index=True)
    gateway_name = models.CharField(max_length=100, null=False, blank=False)
    gateway_description = models.TextField(  null=False, blank=False)
    location = models.ForeignKey(Location, db_column="location_id", on_delete=models.SET_NULL,
                                  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL,
                                    related_name = 'gateway_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='gateway_updated_by', null=True, blank=True)

    def __str__(self) :
        return self.gateway_name   

class Order_payment(models.Model):
    order_payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                                         db_index=True)
    order = models.ForeignKey(Order,  db_column='order_id', on_delete=models.SET_NULL, 
                               related_name = 'order_payment_order', null=True, blank=True)
    amount_paid =  models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    gateway = models.ForeignKey(Gateway, on_delete=models.SET_NULL, 
                                   related_name = 'order_payment_gateway', null=True, blank=True)
    gateway_code = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL,
                                    related_name = 'order_payment_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='order_payment_updated_by', null=True, blank=True)

    # post save update order to is fully paid
    # post save load to sales tables


class Sales(models.Model):
    sale_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                                         db_index=True)
    order = models.ForeignKey(Order,  db_column='order_id', on_delete=models.SET_NULL, 
                               related_name = 'sales_order', null=True, blank=True)
    vendor = models.ForeignKey(Vendor,  db_column='vendor_id', on_delete=models.SET_NULL, 
                               related_name = 'sales_vendor', null=True, blank=True)
    amount_paid =  models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL,
                                    related_name = 'sales_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='sales_updated_by', null=True, blank=True)


class Returned_produce(models.Model):
    returned_produce_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,
                                         db_index=True)
    vendor = models.ForeignKey(Vendor,  db_column='vendor_id', on_delete=models.SET_NULL, 
                               related_name = 'returned_produce_vendor', null=True, blank=True)
    produce = models.ForeignKey(Produce,  db_column='produce_id', on_delete=models.SET_NULL, 
                               related_name = 'returned_produce_produce', null=True, blank=True,  db_index=True)
    unit = models.ForeignKey(Unit, db_column='unit_id', on_delete=models.SET_NULL, 
                             related_name = 'returned_produce_unit', null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    complaint = models.TextField()
    amount_refunded  =  models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    is_given_new_produce =  models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL,
                                    related_name = 'returned_produce_created_by', null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(NewUser, on_delete=models.SET_NULL, 
                                   related_name='returned_produce_updated_by', null=True, blank=True)