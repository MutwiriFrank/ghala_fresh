# Generated by Django 4.2.3 on 2023-07-18 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('gateway_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gateway_name', models.CharField(max_length=100)),
                ('gateway_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gateway_created_by', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, db_column='location_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gateway_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_delivered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_updated_by', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(blank=True, db_column='vendor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_vendor', to='users.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('produce_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('produce_name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('produce_description', models.TextField(blank=True, null=True)),
                ('storage_period', models.CharField(blank=True, choices=[('Less than a week', 'less than a week'), ('less than 2 weeks', 'less than 2 weeks'), ('less than a month', 'less than a month '), ('more than a month', 'more than a month')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produce_created_by', to=settings.AUTH_USER_MODEL)),
                ('source_location_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produce_source_location_1', to='users.location')),
                ('source_location_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produce_source_location_2', to='users.location')),
                ('source_location_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produce_source_location_3', to='users.location')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produce_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product_services',
            fields=[
                ('service_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=100)),
                ('service_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_services_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_services_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Repackaged_produce',
            fields=[
                ('repackaged_produce_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('unit_quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_product_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_repacked', models.DateField(db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repackaged_produce_created_by', to=settings.AUTH_USER_MODEL)),
                ('produce', models.ForeignKey(db_column='produce_id', on_delete=django.db.models.deletion.RESTRICT, related_name='repackaged_produce_produce', to='cms.produce')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('warehouse_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('warehouse_name', models.CharField(max_length=100)),
                ('warehouse_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warehouse_created_by', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, db_column='location_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warehouse_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unit_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('unit_name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('unit_description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unit_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unit_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Units',
                'verbose_name_plural': 'Units',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('unit_quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_created_by', to=settings.AUTH_USER_MODEL)),
                ('produce', models.ForeignKey(blank=True, db_column='produce_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_produuce', to='cms.produce')),
                ('unit', models.ForeignKey(blank=True, db_column='unit_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_unit', to='cms.unit')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_updated_by', to=settings.AUTH_USER_MODEL)),
                ('warehouse', models.ForeignKey(blank=True, db_column='warehouse_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_warehouse', to='cms.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping_from_farm',
            fields=[
                ('shipment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('driver_phone', models.CharField(max_length=13)),
                ('shipping_date', models.DateField(db_index=True, default=django.utils.timezone.now)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_from_farm_created_by', to=settings.AUTH_USER_MODEL)),
                ('transporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_from_farm_transporter', to='users.transporter')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_from_farm_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sale_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_created_by', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, db_column='order_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_order', to='cms.order')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_updated_by', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(blank=True, db_column='vendor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_vendor', to='users.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Returned_produce',
            fields=[
                ('returned_produce_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('complaint', models.TextField()),
                ('amount_refunded', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_given_new_produce', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='returned_produce_created_by', to=settings.AUTH_USER_MODEL)),
                ('produce', models.ForeignKey(blank=True, db_column='produce_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='returned_produce_produce', to='cms.produce')),
                ('unit', models.ForeignKey(blank=True, db_column='unit_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='returned_produce_unit', to='cms.unit')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='returned_produce_updated_by', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(blank=True, db_column='vendor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='returned_produce_vendor', to='users.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Repackaged_produce_to_services',
            fields=[
                ('product_to_service_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('service_quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repackaged_produce_to_services_created_by', to=settings.AUTH_USER_MODEL)),
                ('product_service', models.ForeignKey(db_column='service_id', on_delete=django.db.models.deletion.RESTRICT, to='cms.product_services')),
                ('repackaged_produce', models.ForeignKey(db_column='repackaged_produce_id', on_delete=django.db.models.deletion.RESTRICT, to='cms.repackaged_produce')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repackaged_produce_to_services_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='repackaged_produce',
            name='shipping_from_farm',
            field=models.ForeignKey(db_column='shipment_id', on_delete=django.db.models.deletion.RESTRICT, related_name='repackaged_produce_shipping_from_farm', to='cms.shipping_from_farm'),
        ),
        migrations.AddField(
            model_name='repackaged_produce',
            name='unit',
            field=models.ForeignKey(db_column='unit_id', on_delete=django.db.models.deletion.RESTRICT, related_name='repackaged_produce_unit', to='cms.unit'),
        ),
        migrations.AddField(
            model_name='repackaged_produce',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repackaged_produce_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Received_products',
            fields=[
                ('received_products', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('unit_quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_received', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_products_created_by', to=settings.AUTH_USER_MODEL)),
                ('produce', models.ForeignKey(blank=True, db_column='produce_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_products_produuce', to='cms.produce')),
                ('unit', models.ForeignKey(blank=True, db_column='unit_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_products_unit', to='cms.unit')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_products_updated_by', to=settings.AUTH_USER_MODEL)),
                ('warehouse', models.ForeignKey(blank=True, db_column='warehouse_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_products_warehouse', to='cms.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_produce',
            fields=[
                ('purchase_produce_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date_bought', models.DateField(db_index=True, default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_produce_employee', to='users.employee')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_produce_created_by', to=settings.AUTH_USER_MODEL)),
                ('farmer', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_produce_farmer', to='users.farmer')),
                ('location', models.ForeignKey(blank=True, db_column='location_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_produce_location', to='users.location')),
                ('produce', models.ForeignKey(blank=True, db_column='produce_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_produce_produce', to='cms.produce')),
                ('unit', models.ForeignKey(blank=True, db_column='unit_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_produce_unit', to='cms.unit')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_produce_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Order_payment',
            fields=[
                ('order_payment_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gateway_code', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_payment_created_by', to=settings.AUTH_USER_MODEL)),
                ('gateway', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_payment_gateway', to='cms.gateway')),
                ('order', models.ForeignKey(blank=True, db_column='order_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_payment_order', to='cms.order')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_payment_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('order_item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_item_created_by', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, db_column='order_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_item_order', to='cms.order')),
                ('produce', models.ForeignKey(blank=True, db_column='produce_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_produce', to='cms.produce')),
                ('unit', models.ForeignKey(blank=True, db_column='unit_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_item_unit', to='cms.unit')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_item_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Opening_closing_stock',
            fields=[
                ('opening_closing_stock_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('opening_quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('closing_quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_sold', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opening_closing_stock_created_by', to=settings.AUTH_USER_MODEL)),
                ('produce', models.ForeignKey(blank=True, db_column='produce_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opening_closing_stock_produuce', to='cms.produce')),
                ('unit', models.ForeignKey(blank=True, db_column='unit_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opening_closing_stock_unit', to='cms.unit')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opening_closing_stock_updated_by', to=settings.AUTH_USER_MODEL)),
                ('warehouse', models.ForeignKey(blank=True, db_column='warehouse_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opening_closing_stock_warehouse', to='cms.warehouse')),
            ],
        ),
        migrations.AddIndex(
            model_name='shipping_from_farm',
            index=models.Index(fields=['driver_phone', 'shipping_date'], name='cms_shippin_driver__501b87_idx'),
        ),
    ]
