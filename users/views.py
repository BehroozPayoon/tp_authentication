from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data['username']).first()
        if user and user.check_password(request.data['password']):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class AuthenticateView(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        if not token:
            return Response({'valid': False}, status=status.HTTP_400_BAD_REQUEST)
        try:
            access_token_obj = AccessToken(token)
            user_id = access_token_obj['user_id']
            user = User.objects.get(id=user_id)
            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_authenticated': True
            }, status=status.HTTP_200_OK)
        except (TokenError, InvalidToken):
            return Response({'valid': False}, status=status.HTTP_400_BAD_REQUEST)
