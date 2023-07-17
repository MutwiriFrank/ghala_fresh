from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import request, JsonResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password   
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.hashers import make_password   
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import is_valid_path
from  django.contrib.auth.decorators import login_required
from django.db import transaction

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated,  IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView,)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Farmer, Employee, Location, Produce_buyer_to_farmer
from .serializers import RegisterFarmerSerializer, RegisterVendorSerializer

from .forms import CreateFarmerForm
# from users.decorators  import *


def login_page(request):
    '''
    Login Staff
    '''
    username = password = '' 
    if request.user.is_authenticated:
        return redirect('users:get_farmers')

    else:
        if request.POST:
            phone_number = request.POST.get('phone_number')
            password = request.POST.get('password')
            print(password)
            print(phone_number)
            user = authenticate(request, phone_number=phone_number, password=password)

            if user is not None: 
                # if the user exist in db a session is created and username is used to identify the session
                if user.is_active:
                    # Get a session value by its key
                    request.session['user'] = phone_number
                    login(request, user)
                return redirect('users:get_farmers')

            # else:
        
            #     messages.error(request, "username and password do not match, \n Try again")
            #     return redirect('users:login')
        else:
            return render(request, 'users/login.html',)
        

def logout_page(request):
    logout(request)  # a user is logout
    request.session.flush()  # session is destroyed
    request.user = 'AnonymousUser'
    # print('session deleted')
    return redirect('users:login')


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     def validate(self, attrs):
    
#         try:
#             data = super().validate(attrs)
#             serializer = UserSerializerWithToken(self.user).data          
#             for k, v in serializer.items():
#                 data[k] = v          
#             return data
#         except:
#            raise serializers.ValidationError({'detail':'Wrong phone number or password!'})
                  

# class loginView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


class RegisterFarmerView(APIView):
    '''
    Crate account for new Farmers
    '''
    permission_classes = [AllowAny]
    serializer_class = RegisterFarmerSerializer

    @swagger_auto_schema(request_body=RegisterFarmerSerializer)
    def post(self, request, format='json' ):
        serializer = RegisterFarmerSerializer(data=request.data)

        try:
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    messsage = {'detail': 'User is successfully created'}
                    return Response(messsage,  status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        except:
            messsage = {'detail': 'Error occured when creating your farmer account. Please contact Admin'}
            return Response(messsage, status=status.HTTP_400_BAD_REQUEST)
        

class RegisterVendorView(APIView):
    
    '''
    Crate account for new Vendors
    '''
    
    permission_classes = [AllowAny]
    serializer_class = RegisterVendorSerializer

    @swagger_auto_schema(request_body=RegisterVendorSerializer)
    def post(self, request, format='json' ):
        serializer = RegisterVendorSerializer(data=request.data)

        try:
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    messsage = {'detail': 'User is successfully created'}
                    return Response(messsage,  status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        except:
            messsage = {'detail': 'Error occured when creating your vendor account. Please contact Admin'}
            return Response(messsage, status=status.HTTP_400_BAD_REQUEST)
        

@transaction.atomic
@login_required(login_url='users:login')
def create_farmer(request):
    '''
    Staff should be able to add farmers to the system
    '''
    phone_number = request.POST.get('phone_number')
    print(phone_number)
    # user = request.user
    locations = Location.objects.all()
    context = { 'locations': locations}
    if request.POST:
        phone_number = request.POST.get('phone_number')
        phone_number_2 = request.POST.get('phone_number_2')
        email = request.POST.get('email')
        full_names = request.POST.get('full_names')
        resp_location = request.POST.get('location')
        resp_is_broker = request.POST.get('is_broker')
        password = request.POST.get('password')

        resp_location = request.POST.get('location')
        location = Location.objects.filter(location_id =resp_location ).first()
        is_broker = False
        if resp_is_broker == 'on' :
            is_broker = True

        print(phone_number)

        if phone_number=='' or phone_number is None :
            messages.warning(request, 'Please input your phone number.')
            return render(request, 'users/create_farmer.html',)
        

        if full_names is None:
            message = 'Please input your phone number'
            context ={'message':  message}
            return render(request, 'users/create_farmer.html', context)
        

        if location is None:
            message = 'Please input your phone number'
            context ={'message':  message}
            return render(request, 'users/create_farmer.html', context)
        
        if password is None:
            password = "ghalafreshfoods"
            

        farmer = Farmer(phone_number=phone_number, phone_number_2=phone_number_2, full_names=full_names,
                        location=location,  is_broker=is_broker, email=email )
        
        farmer.set_password(password)

        farmer.save()

        buyer = Employee.objects.filter(user_id = request.user.user_id).first()
        bridge = Produce_buyer_to_farmer(farmer = farmer, produce_buyer = buyer )
        bridge.save()

        
    
    return render(request, 'users/create_farmer.html', context)
        
    # except:
    #     message = 'Error when submitting the form'
    #     context ={'message':  message}
    #     return render(request, 'users/create_farmer.html', context)
    
    
# @(buyers & admin)
@login_required(login_url='users:login')
def get_farmers(request):
    '''
    Produce BUyers should be able to view only the farmers they added
    '''
    user = request.user
    employee = Employee.objects.filter(user_id = user.user_id).first()
    context = {}

    if request.method == 'GET':
        farmers = Farmer.objects.filter(Produce_buyer_to_farmer__produce_buyer=employee )
        context = {
            'farmers': farmers
        } 
        return render(request, 'users/get_farmers.html', context)


   
@login_required(login_url='users:login')
def update_farmer(request, id):
    farmer = Farmer.objects.filter(user_id=id).first()
    locations = Location.objects.all()
    if request.POST:
        farmer.phone_number = request.POST.get('phone_number')
        farmer.phone_number_2 = request.POST.get('phone_number_2')
        farmer.email = request.POST.get('email')
        farmer.full_names = request.POST.get('full_names')
        resp_location = request.POST.get('location')
        farmer.location =  Location.objects.filter(location_id =resp_location ).first()
        resp_is_broker = request.POST.get('is_broker')
        
        if resp_is_broker == 'on' :
            farmer.is_broker = True
        farmer.save()

    context = {"farmer":farmer, "locations" : locations}
    



    











    


    











# get all farmers




# @transaction.atomic
# update farmer




#soft delete farmer




