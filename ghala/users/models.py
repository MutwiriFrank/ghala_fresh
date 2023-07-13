from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

import random
import uuid

class CustomAccountManager(BaseUserManager):

    def create_superuser(self,  full_names,  phone_number,  password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user( full_names,   phone_number,   password, **other_fields)

    def create_user(self,  full_names,  phone_number,   password, **other_fields):

        if not phone_number:
            raise ValueError(('You must provide a phone number'))

        # email = self.normalize_email(email)
        user = self.model(full_names=full_names, phone_number=phone_number,  
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser( AbstractBaseUser, PermissionsMixin ):

    # groups = models.ManyToManyField(Group, verbose_name=('groups'),
    # blank=True,
    # related_name='new_user_set',  # Change the related_name for groups
    # related_query_name='new_user'
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=('user permissions'),
    #     blank=True,
    #     related_name='new_user_set',  # Change the related_name for user_permissions
    #     related_query_name='new_user'
    # )
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    full_names = models.CharField(max_length=100 )
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False) # people who can access admin
    is_active = models.BooleanField(default=True    )
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=12, blank=False, null=False, unique=True)
    phone_number_2 = models.CharField(max_length=12, blank=True, null=True,)
    otp = models.CharField(max_length=6, null=True, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_names']

    def __str__(self):
        return self.full_names

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]  # Use of list comprehension
        code_items_for_otp = []

        for i in range(6):
            num = random.choice(number_list)
            code_items_for_otp.append(num)

        code_string = "".join(str(item)
        for item in code_items_for_otp)  # list comprehension again
        # A six digit random number from the list will be saved in top field
        self.otp = code_string
        super().save(*args, **kwargs)


class Location(models.Model):
    location_id = models.CharField(max_length=100, blank=False, null=False, unique=True, primary_key=True)
    location_name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    county = models.CharField(max_length=255, blank=False, null=False)
    region = models.CharField(max_length=255, blank=False, null=False)

  
    def __str__(self):
        return self.location_name
    

class Farmer(NewUser):
    location = models.ForeignKey(Location, db_column="location_id", on_delete=models.SET_NULL, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null = True, blank=True )
    is_broker = models.BooleanField(default=False)
    
    def __str__(self):
        return self.full_names
    
class Vendor(NewUser):
    location = models.ForeignKey(Location, db_column="location_id", on_delete=models.SET_NULL, null=True, blank=True)
    business_name = models.CharField(max_length=100, null=True, blank=True)
    kra_pin = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null = True, blank=True )

    def __str__(self):
        return self.full_names
    

class Employee(NewUser):
    location = models.ForeignKey(Location, db_column="location_id", on_delete=models.SET_NULL, null=True, blank=True)
    position =   models.CharField(max_length=100, null=True, blank=True)
    experience_years = models.DecimalField(max_digits=9, decimal_places=3, null=True, blank=True)
    hire_date =  models.DateField (null=True, blank=True)
    is_rehired =  models.BooleanField(default=False)
    salary = models.DecimalField(max_digits=9, decimal_places=3, null=True, blank=True)
    commission = models.DecimalField(max_digits=9, decimal_places=3, null=True, blank=True)
    
    def __str__(self):
        return self.full_names
    

class Transporter(NewUser):
    registration_number= models.CharField(max_length=100, blank=True, null=True)
    owner_phone_number =  models.CharField(max_length=12, blank=True, null=True, unique=True)
    capacity_kg = models.DecimalField(max_digits=9, decimal_places=3, null=True, blank=True)
    vehicle_brand =   models.CharField(max_length=100, blank=True, null=True)
    location = models.ForeignKey(Location, db_column="location_id", on_delete=models.SET_NULL, null=True, blank=True)
    is_broker = models.BooleanField(default=False, blank=True, null=True, )
    
    def __str__(self):
        return self.full_names
    

