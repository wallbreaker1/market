
from datetime import datetime
from typing import List

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserAccountManager(BaseUserManager):
    def create_user(self, email: str, password: str = None, **extra_fields):
        if not email:
            raise ValueError("User account must have an email address")
        
        email = self.normalize_email(email).lower()
        
        user: UserAccount = self.model(email=email, **extra_fields)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email: str, password: str, **extra_fields):
        user: UserAccount = self.create_user(email, password, **extra_fields)
        
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        
        user.save(using=self._db)
        
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name: str = models.CharField(max_length=50)
    last_name : str = models.CharField(max_length=50)
    
    email: str = models.CharField(max_length=250, unique=True)
    password: str= models.CharField(max_length=250)

    is_active: bool = models.BooleanField(default=True)
    is_staff: bool = models.BooleanField(default=True)
    
    create_at: datetime = models.DateTimeField(auto_now_add=True)
    updated_at: datetime = models.DateTimeField(auto_now=True)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = ["first_name", "last_name"]

    
    class Meta:
        db_table = "user_account"
        ordering = ["-create_at"]
        
    def __str__(self) -> str:
        return self.email
    
    
    
    

    