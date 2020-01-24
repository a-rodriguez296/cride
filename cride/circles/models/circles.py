from django.db import models

from cride.utils.models import CRideModel


class Circle(CRideModel):

    """A circle is a private group that allows members to offer carpool rides"""


    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(
        upload_to='circles/pictures',
        blank=True,
        null=True
    )

    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles have been verified as official communities'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Allow circles to be listed or not. Private circles will not be listed publicly'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members'
    )

    members_limit = models.PositiveIntegerField(
        default=0, 
        help_text='If circle is limited, this will be the limit on the number of members'
    )

    def __str__(self):
        return self.name

    class Meta(CRideModel.Meta):
        # Esto se hace para sobre escribir el ordering que ya viene definido en la clase meta
        ordering= ['-rides_taken', '-rides_offered']




