from django.urls import path
from .views import TokenObtainPairView, TokenRefreshView, CreateUserView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', CreateUserView.as_view(), name='create_user'),
]

