from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import *
from rest_framework.generics import *
from rest_framework.response import Response

# Create your views here.

class UsersDetailView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"

class UserUpdatePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordSerializer
    lookup_field = "id"

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                tokens = serializer.validated_data['tokens']
                return Response({'token': tokens}, status=200)
        else:
            return Response(serializer.errors, status=401)