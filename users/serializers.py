import re
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth

from .registration_validators import validate_number
from django.contrib.auth import password_validation
from rest_framework import serializers, exceptions

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, min_length=6,
                                     help_text=password_validation.password_validators_help_texts(), write_only=True,
                                     style={'input_type': 'password'})
    first_name = serializers.CharField(max_length=30, min_length=2,
                                       help_text='Firstname should contain only alphanumeric characters')
    last_name = serializers.CharField(max_length=30, min_length=2,
                                      help_text='Lastname should contain only alphanumeric characters')
    email = serializers.EmailField(max_length=30, min_length=5,
                                   help_text='Username should contain only alphanumeric characters')
    number = serializers.CharField(max_length=9,
                                   help_text=['Numbers length is should be 9', 'Number should contain only digits'])
    username = serializers.CharField(max_length=30, min_length=2)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'number']

    def validate(self, attrs):
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        username = attrs.get('username', '')
        validate = (first_name, last_name, username)
        for value in validate:
            if not value.isalnum():
                raise serializers.ValidationError('The user datas should only contain alphanumeric characters')
        return super().validate(attrs)

    def validate_number(self, number):
        char = re.findall(r'(?:[a-zA-Z])', number.lower())
        if len(char) != 0:
            raise exceptions.ValidationError('Number should contain only digits')
        return number

    def validate_password(self, password):
        errors = {}
        try:
            password_validation.validate_password(password=password)
        except exceptions.ValidationError as exc:
            errors['password'] = list(exc.get_codes())
        if errors:
            raise serializers.ValidationError(str(errors))
        return password

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        number = validated_data.pop('number', None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)
        if number:
            try:
                validate_number(number)
            except exceptions.ValidationError as error:
                raise serializers.ValidationError(f'error: {error.get_codes()}')
            else:
                user.number = f'+996{number}'
        else:
            raise serializers.ValidationError('no number')
        user.save()
        return user


class EmailVerifySerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=5)
    password = serializers.CharField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=30, min_length=3, read_only=True)
    tokens = serializers.CharField(max_length=60, min_length=8, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account is disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        return {
            'email': user.email,
            'username': user.username,
            'number': user.number,
            'tokens': user.tokens(),
        }

