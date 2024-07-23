from unicodedata import category
from django.db import models

from django.utils import timezone
# from django.db.backends.mysql.base import DatabaseWrapper

# DatabaseWrapper.data_types = DatabaseWrapper._data_types

from django.contrib.auth.models import AbstractUser, AbstractBaseUser


from .managers import CustomUserManager

class Centers(models.Model):
    name= models.TextField()

    class Meta:
        db_table='centers'

class Images(models.Model):
    link= models.TextField()
    name= models.TextField()

    class Meta:
        db_table='images'

class Colors(models.Model):
    name= models.TextField()
    color_code_hex= models.TextField()

    class Meta:
        db_table='colors'