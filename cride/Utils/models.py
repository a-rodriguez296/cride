from django.db import models 

class CRideModel(models.Model):
    '''
    atributos para que cada vez que se crea un modelo se guarde la fecha y tambien cada vez que 
    se actualize.
    '''

    created = models.DateTimeField(
        'created at',
        auto_now_add =True,
        help_text='Date time in which the object was created.'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now =True,
        help_text='Date time in which the object was modified.'
    )

    class Meta:

        ''' Esto es para que no se cree una tabla en la base de datos. Esta es una clase abstracta.'''
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']

