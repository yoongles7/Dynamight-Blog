from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserLogoutSerializer,
    UserSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        
        token = get_tokens_for_user(user)
        
        return Response(
            {"token": token,
             "msg": "Registration Successful!"},
            status = status.HTTP_201_CREATED,
        )
        
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        
        user = authenticate(email=email, password=password)
        
        if user is None:
            return Response(
                {errors: {"non_field_error": ["email or password not valid"]}},
                status = status.HTTP_401_UNAUTHORIZED,
            )
            
        token = get_tokens_for_user(user)
        
        return Response(
            {"token": token,
             "msg": "Login Successfull!"},
            status = status.HTTP_200_OK,
        )
        
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = UserLogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(
            {"msg": "Logout Successfull!"},
            status = status.HTTP_200_OK
        )