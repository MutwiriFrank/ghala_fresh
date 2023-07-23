# Generated by Django 4.2.3 on 2023-07-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_rename_received_products_received_products_received_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='unit_quantity',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='stock',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
