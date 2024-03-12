from django.db import models
from django.contrib.auth.base_user import BaseUserManager

class AuthorManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if not username:
            raise ValueError('User must provide an username')
        
        if not email:
            raise ValueError('User must provide an email')
        
        user = self.model(
        username = self.model.normalize_username(username),
        email = self.normailize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db) # why do we do this?
        
        return user


    def create_superuser(self, username, email, password=None):
        if not username:
            raise ValueError('User must provide an username')
        
        if not email:
            raise ValueError('User must provide an email')
        
        user = self.create_user(
        username = self.model.normalize_username(username),
        email = self.normailize_email(email),
        password = password # why do we do this and ont how it is in create_user?
        ) # superuser just call the create_user method. Then it sets the necessary fields on the user model to Tru to denote an admin user

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db) # why do we do this?

        return user