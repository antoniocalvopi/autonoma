from django.urls import path
from .views import TokenObtainPairView, TokenRefreshView, CreateUserView, LogoutView, UpdateUserProfileView, GetUserProfileView, verify_token

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/revoke/', LogoutView.as_view(), name='token_revoke'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('update/', UpdateUserProfileView.as_view(), name='update_profile'),
    path('profile/', GetUserProfileView.as_view(), name='get_profile'),
]