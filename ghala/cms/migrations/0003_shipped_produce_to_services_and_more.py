# Generated by Django 4.2.3 on 2023-07-18 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0002_produce_ship_from_farm_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipped_produce_to_services',
            fields=[
                ('product_to_service_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('service_quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipped_produce_to_services_created_by', to=settings.AUTH_USER_MODEL)),
                ('product_service', models.ForeignKey(blank=True, db_column='service_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.product_services')),
                ('shipped_produce', models.ForeignKey(blank=True, db_column='shipment_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.produce_ship_from_farm')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipped_produce_to_services_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Repackaged_produce_to_services',
        ),
    ]
