from django.contrib.auth import authenticate, password_validation
from rest_framework import serializers
from rest_framework.authtoken.models import Token 
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator

from cride.users.models import User, Profile

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = User 
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )

class UserSignupSerializer(serializers.Serializer):
    
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        min_length=4,
        max_length=20
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format +9999999999. Up to 15 digits'
    )

    phone_number = serializers.CharField(validators=[phone_regex])

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name=serializers.CharField(min_length=2, max_length=30)
    last_name=serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        #Verify that passwords match
        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if not passwd == passwd_conf:
            raise serializers.ValidationError("Passwords do not match")

        password_validation.validate_password(passwd)
        return data 

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False)
        profile = Profile.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        print("entro validate")
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_verified:
            raise serializers.ValidationError('Account has not been verified')
        self.context['user'] = user
        return data


    def create(self, data):
        print("entro create")
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


