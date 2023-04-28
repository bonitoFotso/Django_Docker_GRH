from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='profile', blank=True, null=True)
    username = models.CharField(max_length=50,null=True,blank=True)

    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()


class Reset(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)


