from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CuatomUserManager(BaseUserManager):
    def create_user(self, username, email, password = None, **extra_fields):
        if not email:
            raise ValueError('Email Address is Required')
        
        if not password:
            raise ValueError('Password is Required')
        try:
                user = self.model(
                    email = self.normalize_email(email),
                    username =username
                    **extra_fields 
                )
                user.set_password(password)
                user.save()
                return user
        except:
             raise ValueError('An Error Occured Please Try Again') 
        

    def create_superuser(self, email, username,password=None, **extra_fields):
        try:
            user = self.create_user(
                    email,
                    username=username,
                    password=password,
                    is_admin=True,
                    is_superuser=True,
                    is_staff=True,
                    **extra_fields,
            )
            
            return user
        except:
               raise ValueError('An Error Occured Please Try Again')
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # USERNAME_FIELD = username
    REQUIRED_FIELDS = ['email']
