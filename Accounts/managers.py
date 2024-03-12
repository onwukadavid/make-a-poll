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
        
        user = self.model(
        username = self.model.normalize_username(username),
        email = self.normailize_email(email),
        password = password # why do we do this and ont how it is in create_user?
        )
        user.is_admin = True
        user.save(using=self._db) # why do we do this?

        return user