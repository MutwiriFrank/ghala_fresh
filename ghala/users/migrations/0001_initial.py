# Generated by Django 4.2.3 on 2023-07-18 10:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('full_names', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('phone_number', models.CharField(db_index=True, max_length=12, unique=True)),
                ('phone_number_2', models.CharField(blank=True, max_length=12, null=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_edited', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='newuser_created_by', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('newuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('position', models.CharField(blank=True, choices=[('sales_person', 'sales person'), ('produce_buyer', 'produce buyer')], null=True)),
                ('experience_years', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('is_rehired', models.BooleanField(blank=True, default=False, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('commission', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
            options={
                'permissions': (('can_add_farmers', 'Can add farmers'), ('can_add_vendors', 'Can add Vendors'), ('can_list_farmers', 'Can list farmers'), ('can_list_vendors', 'Can list vendors'), ('can_list_orders', 'Can list orders')),
            },
            bases=('users.newuser',),
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('newuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('is_broker', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.newuser',),
        ),
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('newuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('registration_number', models.CharField(blank=True, max_length=100, null=True)),
                ('owner_phone_number', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('capacity_kg', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('vehicle_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('is_broker', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.newuser',),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('newuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('business_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
                ('kra_pin', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.newuser',),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('location_name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('county', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_edited', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='newuser',
            name='location',
            field=models.ForeignKey(blank=True, db_column='location_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='newuser_location', to='users.location'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='newuser_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='newuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Produce_buyer_to_farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True, null=True)),
                ('end_date', models.DateField(blank=True, default=datetime.date(2099, 12, 31), null=True)),
                ('farmer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Produce_buyer_to_farmer', to='users.farmer')),
                ('produce_buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Produce_buyer_to_farmer', to='users.employee')),
            ],
        ),
    ]
