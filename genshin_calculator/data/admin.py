from django.contrib import admin

from .models import Character

app_name = 'data'


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'element', 'weapon')


admin.site.register(Character, CharacterAdmin)
