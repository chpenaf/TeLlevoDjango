from django.urls import path

from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)

from .views import (
  changePassword,
  driverTripView,
  userDetailGet,
  userUpdate,
  sendEmailRecoveryPassword
)

urlpatterns = [
  #SimpleJWT
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

  #Api
  path('user/' , userDetailGet, name='user-detail'),
  path('user/update/' , userUpdate, name='user-update'),
  path('user/update-password/' , changePassword, name='password-update'),
  path('user/<str:username>', sendEmailRecoveryPassword, name='recovery-password' ),

  path('driver/trip/', driverTripView, name='driver-trip')

]
