from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, password, number):
        if username is None:
            raise TypeError('Users should have username')
        if email is None:
            raise TypeError('Users should have email')
        user = self.model(username=username, first_name=first_name, last_name=last_name,
                          email=self.normalize_email(email), number=number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, email, password, number):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(username, first_name, last_name, email, password, number)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    password = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, db_index=True)
    number = models.CharField(max_length=255, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False, help_text='Сотрудник')
    is_superuser = models.BooleanField(default=False, help_text='админ')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name', 'first_name', 'number']
    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
