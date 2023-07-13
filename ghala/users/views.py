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

from .models import Farmer, NewUser
from .serializers import RegisterFarmerSerializer, RegisterVendorSerializer


def login_page(request):
    '''
    Login Staff
    '''
    username = password = '' 
    if request.user.is_authenticated:
        return redirect('schema-swagger-ui')

    else:
        if request.POST:
            phone_number = request.POST.get('phone_number')
            password = request.POST.get('password')
            print(password + phone_number)
            user = authenticate(request, phone_number=phone_number, password=password)

            if user is not None: 
                # if the user exist in db a session is created and username is used to identify the session
                if user.is_active:
                    # Get a session value by its key
                    request.session['user'] = phone_number
                    login(request, user)
                return redirect('')

            else:
        
                messages.error(request, "username and password do not match, \n Try again")
                return redirect('users:login')
        else:
            return render(request, 'users/login.html',)



def logout_page(request):
    logout(request)  # a user is logout
    request.session.flush()  # session is destroyed
    request.user = 'AnonymousUser'
    # print('session deleted')
    return redirect('login')


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
        


