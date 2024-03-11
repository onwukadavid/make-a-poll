from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .managers import AuthorManager


# This is done so that I can change the User Model mid project without any issues. 
class User(AbstractUser):
    pass

# create cuntom user model
class Author(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email    = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    verified_at = models.DateTimeField()
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = AuthorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', 'password']

    def get_username(self):
        return self.username
    
    def __str__(self):
        return self.email
    
    # SET PERMISSIONS BEFORE SWAPPING 
    class Meta:
        permissions = [
            ('can_ban_user', 'Can ban users')
        ]