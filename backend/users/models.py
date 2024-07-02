from asgiref.sync import sync_to_async
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields) -> "User":
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    async def acreate_user(self, email, password, **extra_fields) -> "User":
        return await sync_to_async(self.create_user)(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields) -> "User":
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

    async def acreate_superuser(self, email, password=None, **extra_fields) -> "User":
        return await sync_to_async(self.create_superuser)(
            email, password, **extra_fields
        )


user_manager = UserManager()


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = user_manager

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
