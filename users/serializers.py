from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# class LoginSerializer(serializers.ModelSerializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ('username', 'password')

#     def validate(self, attrs):
#         user = authenticate(**attrs)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Invalid credentials")

#     def create(self, validated_data):
#         user = self.validated_data
#         refresh = RefreshToken.for_user(user)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }
