from django.contrib import admin
from django.contrib import admin

from cride.circles.models import Circle

"""
Para los modelos comunes y corrientes se debe usar este decorador.
Para clases como user, si de debe hacer la inscripción
admin.site.register(User, CustomUserAdmin)
"""
@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limited',
        'members_list'
    )

    search_fields = ('slug_name', 'name')
    list_filter = (
        'is_public',
        'verified',
        'is_limited'
    )