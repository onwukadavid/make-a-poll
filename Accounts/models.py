from django.db import models
from django.contrib.auth.models import AbstractUser


# This is done so that I can change the User Model mid project without any issues. 
class User(AbstractUser):
    pass
