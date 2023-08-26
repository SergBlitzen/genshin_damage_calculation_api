from django.contrib import admin

from .models import Character, Weapon

app_name = 'data'


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'element', 'weapon')


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'substat_name')
