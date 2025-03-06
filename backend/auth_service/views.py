# auth_service/views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User  # O el modelo de usuario que estés utilizando
from rest_framework import status
from .serializers import UserSerializer  # Asegúrate de tener este serializer

# Vista personalizada para obtener el token
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Vista personalizada para obtener el JWT, con la posibilidad de agregar
    lógica extra, como el seguimiento de actividad o añadir datos personalizados
    al token.
    """
    def get_serializer_class(self):
        # Puedes modificar el serializer si deseas personalizar los datos de entrada/salida
        return super().get_serializer_class()

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response

# Vista personalizada para refrescar el token
class CustomTokenRefreshView(TokenRefreshView):
    """
    Vista personalizada para refrescar el JWT, con la posibilidad de agregar
    lógica extra antes de devolver el nuevo token.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response

# Vista para revocar un token (opcional)
class LogoutView(APIView):
    """
    Vista para manejar la revocación del JWT cuando el usuario cierra sesión.
    """
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Token revocado con éxito."}, status=200)
        except Exception as e:
            return Response({"detail": "Error al revocar el token."}, status=400)

# Vista para crear un usuario
class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)