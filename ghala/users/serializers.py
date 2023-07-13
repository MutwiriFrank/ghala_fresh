from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .models import (Farmer, Vendor, NewUser)


class RegisterFarmerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False )
    full_names = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    phone_number_2 = serializers.CharField(required=False)
    password = serializers.CharField(min_length=8, write_only=True)
    is_broker = serializers.BooleanField(required=False)


    class Meta:
        model = Farmer
        fields =  ['email', 'full_names', 'phone_number', 'phone_number_2' , 'location', 'is_broker', 'password']
       
        
    def create(self, validated_data):
        user = Farmer(
            email = validated_data['email'],
            full_names = validated_data['full_names'],
            phone_number = validated_data['phone_number'],
            phone_number_2 = validated_data['phone_number_2'],
            location = validated_data['location'],
            is_broker = validated_data['is_broker'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate_email(self, email):
        users = Farmer.objects.filter(email=email)
        if users : 
            raise serializers.serializers.ValidationError('email is invalid')    
        return email
    
    def validate_phone_number(self, phone_number):
        users = Farmer.objects.filter(phone_number=phone_number)
        if users : 
            raise serializers.serializers.ValidationError('email is invalid')    
        return phone_number
    

class RegisterVendorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False )
    full_names = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    phone_number_2 = serializers.CharField(required=False)
    password = serializers.CharField(min_length=8, write_only=True)
    kra_pin = serializers.CharField(required=False)
    business_name = serializers.CharField(required=False)

    class Meta:
        model = Vendor
        fields =  ['email', 'full_names', 'phone_number', 'phone_number_2' , 'location', 
                   'kra_pin','business_name', 'password']
       
        
    def create(self, validated_data):
        user = Vendor(
            email = validated_data['email'],
            full_names = validated_data['full_names'],
            phone_number = validated_data['phone_number'],
            phone_number_2 = validated_data['phone_number_2'],
            location = validated_data['location'],
            kra_pin = validated_data['kra_pin'],
            business_name = validated_data['business_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate_email(self, email):
        users = Vendor.objects.filter(email=email)
        if users : 
            raise serializers.serializers.ValidationError('email is invalid')    
        return email
    
    def validate_phone_number(self, phone_number):
        users = Vendor.objects.filter(phone_number=phone_number)
        if users : 
            raise serializers.serializers.ValidationError('email is invalid')    
        return phone_number
    



