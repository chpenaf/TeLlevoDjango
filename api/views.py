
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import User
from .serializers import (
  DriverTripSerializer,
  UserSerializer,
  UserSerializer2
)

@api_view(['GET'])
def userDetailGet(request: Request):

  if request.method == 'GET':

    user_serializer = UserSerializer( request._user, context={'request': request} )

    return Response(
      user_serializer.data,
      status=status.HTTP_200_OK
    )

@api_view(['PUT'])
def userUpdate(request: Request):

  if request.method == 'PUT':

    user: User = request._user

    user_serializer = UserSerializer(user, data = request.data, context={'request': request})

    if user_serializer.is_valid():

      user_serializer.save()

      return Response(
        user_serializer.data,
        status=status.HTTP_200_OK
      )

    else:

      return Response(
        user_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )

@api_view(['GET'])
def sendEmailRecoveryPassword(request, username):

  if request.method == 'GET':

    user: User = User.objects.all().filter( username = username ).first()

    if user:

      user_serializer = UserSerializer2( user )

      return Response(
        user_serializer.data,
        status=status.HTTP_200_OK
      )

    else:

      return Response(
        { 'error':'No se encontró usuario' },
        status=status.HTTP_404_NOT_FOUND )

@api_view(['PUT'])
def changePassword( request: Request ):

  if request.method == 'PUT':

    user: User = request._user

    old_password = request.data['old_passwd']
    new_password = request.data['new_passwd']

    if user.check_password( old_password ):
      user.set_password( new_password )
      user.save()
      user_serializer = UserSerializer2( user )
      return Response(
        user_serializer.data, status=status.HTTP_200_OK
      )

    else:
      return Response({
        'error':'Contraseña no válida'
      }, status=status.HTTP_409_CONFLICT)

@api_view(['POST'])
def driverTripView(request: Request):

  if request.method == 'POST':

    drivertrip_serializer = DriverTripSerializer( data=request.data )

    if drivertrip_serializer.is_valid():

      drivertrip_serializer.save()

      return Response(
        drivertrip_serializer.data,
        status=status.HTTP_200_OK
      )

    else:

      return Response(
        drivertrip_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )
