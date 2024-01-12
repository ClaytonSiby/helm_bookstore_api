from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class RegisterView(APIView):
    def post(self, request):
        # Retrieve the username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if the username or password is missing
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        
        # generate a token for the user
        try:
            token = Token.objects.get(user=user)
        except ObjectDoesNotExist:
            token = Token.objects.create(user=user)
        
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

class LoginView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Get or create the token for the user
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # Get the user's token
        token = Token.objects.get(user=request.user)
        
        # Delete the token
        token.delete()
        
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)