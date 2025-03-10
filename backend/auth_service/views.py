# auth_service/views.py
from tokenize import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User 
from rest_framework import status
from .serializers import UserSerializer  
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication


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

class GetUserProfileView(APIView):
    """
    Vista para obtener el perfil del usuario autenticado.   
    """
    def get(self, request, *args, **kwargs):
        # Obtener el token desde el encabezado 'Authorization'
        auth_header = request.headers.get('Authorization')

        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]  # Extraer el token después de 'Bearer'
            try:
                # Validar el token con SimpleJWT
                access_token = AccessToken(token)
                
                # Obtener el usuario asociado al token
                user = User.objects.get(id=access_token['user_id'])  

                # Serializar la información del usuario
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except (TokenError, Exception) as e:
                return Response({"detail": "Token inválido o expirado."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"detail": "No se proporcionó un token válido en el encabezado."}, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserProfileView(APIView):
    """
    Vista para actualizar el perfil del usuario autenticado.
    """
    def put(self, request, *args, **kwargs):
        # Obtener el token desde la cabecera de autorización
        auth_header = request.headers.get('Authorization')

        if auth_header:
            try:
                # El formato de la cabecera de autorización es 'Bearer <token>'
                token = auth_header.split(' ')[1]
                
                # Validar el token con SimpleJWT
                access_token = AccessToken(token)
                
                # Obtener el usuario asociado al token
                user = User.objects.get(id=access_token['user_id'])  # Acceso al user_id en el token
            except (IndexError, ValueError):
                return Response({"detail": "Token mal formado."}, status=status.HTTP_400_BAD_REQUEST)
            except (InvalidToken, TokenError) as e:
                return Response({"detail": "Token inválido o expirado."}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({"detail": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

            # Si el token es válido, proceder a actualizar el perfil
            serializer = UserSerializer(user, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()  # Guardar los cambios en el usuario
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"detail": "No se proporcionó token."}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def verify_token(request):
    auth = JWTAuthentication()
    header = request.headers.get("Authorization", "").split("Bearer ")[-1]
    
    if not header:
        return Response({"error": "Token no proporcionado"}, status=401)

    try:
        auth.get_validated_token(header)
        return Response({"message": "Token válido"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=401)