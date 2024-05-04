from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
import jwt

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        payload = {"user_id":user.id,"username":username,"is_staff":user.is_staff}
        token = jwt.encode(payload, settings.SECRET_KEY)
        attrs['tokens'] = token
        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email','first_name','last_name']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data.pop('password'))
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name']

class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','password']

    def update(self, validated_data):
        user = User.objects.get(id=validated_data.pop('id'))
        user.set_password(validated_data.pop('password'))
        user.save()
        return user
    