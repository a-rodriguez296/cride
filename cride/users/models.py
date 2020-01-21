"""Users Model"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utilities
from cride.utils.models import CRideModel

class User(CRideModel, AbstractUser):

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with such email already exists'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format +9999999999. Up to 15 digits'
    )
    phone_number = models.CharField(
        max_length=17, 
        blank=True,
        validators=[phone_regex]
        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Distinguish users and perform queries. '
            'Clients are the main type of uers.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user has validated his email address.'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username 