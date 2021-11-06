from rest_framework import serializers

from .models import DriverTrip, User

class UserSerializer( serializers.ModelSerializer ):

  avatar_url = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = (
      'id',
      'username',
      'name',
      'email',
      'avatar_url'
    )

  def get_avatar_url(self, user:User):
    request = self.context.get('request')
    avatar_url = user.avatar.url
    return request.build_absolute_uri(avatar_url)

class UserSerializer2( serializers.ModelSerializer ):

  class Meta:
    model = User
    fields = (
      'id',
      'username',
      'name',
      'email'
    )

class DriverTripSerializer( serializers.ModelSerializer ):

  class Meta:
    model = DriverTrip
    fields = '__all__'
