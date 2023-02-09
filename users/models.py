from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.utils import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions


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
        datas = (username, number, email)
        for data in datas:
            try:
                user.save()
            except IntegrityError:
                raise exceptions.ValidationError(f'This {data} is not available, please write another one')
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
    username = models.CharField(max_length=255, unique=True, db_index=True)
    number = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False, help_text='Email activated')
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
