# Generated by Django 4.2.3 on 2023-07-23 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_rename_unit_quantity_stock_quantity_stock_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='unit_price',
        ),
    ]
