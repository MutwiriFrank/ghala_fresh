# Generated by Django 4.2.3 on 2023-07-21 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_shipped_produce_to_services_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produce_ship_from_farm',
            old_name='total_product_cost',
            new_name='total_produce_cost',
        ),
    ]
