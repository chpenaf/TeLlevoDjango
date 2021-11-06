from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.timezone import now

class UserManager(BaseUserManager):

    def create_user(self, username, email, name, password=None):
        """ Creacion nuevo usuario """
        if not email:
            raise ValueError('Usuario debe tener Email')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, name, password):
        """ Creacion super usuario """
        user = self.create_user(username, email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
      max_length=150,
      unique=True
    )

    email = models.EmailField(
      max_length=255,
      unique=True
    )

    name = models.CharField(
      max_length=150
    )

    avatar = models.ImageField(
      verbose_name='Avatar',
      upload_to='users',
      null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_full_name(self):
        """ Obtener nombre completo """
        return self.name

    def get_short_name(self):
        """ Obtener nombre corto """
        return self.name

    def __str__(self):
        """ Retorna cadena representativa de usuario """
        return self.get_full_name()

class DriverTrip( models.Model ):

  driver = models.ForeignKey(
      User,
      verbose_name='Conductor',
      on_delete=models.CASCADE)

  origen = models.CharField(
      verbose_name='Origen',
      max_length=500
  )

  destino = models.CharField(
      verbose_name='Destino',
      max_length=500
  )

  hora_salida = models.TimeField(
      verbose_name='Hora Salida'
  )

  fecha_salida = models.DateField(
    verbose_name='Fecha'
  )

  cantidad_pasajeros = models.IntegerField(
    verbose_name='Cantidad pasajeros',
    default=4
  )

  pasajeros = models.ManyToManyField(
    User,
    verbose_name='Pasajeros',
    related_name='usuario_pasajero'
  )

  class Meta:
    verbose_name = 'Viaje conductor'
    verbose_name_plural = 'Viajes conductores'
