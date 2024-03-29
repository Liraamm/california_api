from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string

class UserManager(BaseUserManager):
    def create_user(self,email, password, **kwargs: Any) -> Any:
        if not email:
            raise ValueError(
                'Требуется имэйл'
            )
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.create_activation_code()
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        if not email:
            raise ValueError(
                'Требуется имэйл'
            )
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=10, blank=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self) -> str:
        return f'{self.email} -> {self.id}'
    
    def create_activation_code(self):
        code = get_random_string(length=10, allowed_chars='1234567890')
        self.activation_code = code