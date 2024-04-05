from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from .managers import AuthorManager


# This is done so that I can change the User Model mid project without any issues. 
# class User(AbstractUser):
#     pass

# create custom user model
class Author(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email    = models.EmailField(max_length=50, unique=True)
    password = models.TextField()
    verified_at = models.DateTimeField(null=True)
    is_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 

    objects = AuthorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def get_username(self):
        return self.email
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    
    def __str__(self):
        return self.email
    
    class Meta:
        permissions = [
            ('can_ban_user', 'Can ban users')
        ]

    @property
    def is_staff(self):
        return self.is_admin
