from django.contrib import admin

from .models import Character

app_name = 'data'


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'element', 'weapon')
