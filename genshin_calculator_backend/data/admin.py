from django.contrib import admin

from .models import Character, CharHP, CharNormAtk, Move, CharAtk, CharDef, CharSkill, CharBurst

app_name = 'data'


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'element', 'weapon']


@admin.register(CharHP)
class CharHPAdmin(admin.ModelAdmin):
    list_display = ['character']


@admin.register(CharAtk)
class CharAtkAdmin(admin.ModelAdmin):
    list_display = ['character']


@admin.register(CharDef)
class CharDefAdmin(admin.ModelAdmin):
    list_display = ['character']


@admin.register(CharNormAtk)
class CharNormAtkAdmin(admin.ModelAdmin):
    list_display = ['character']


@admin.register(CharSkill)
class CharSkillAdmin(admin.ModelAdmin):
    list_display = ['character']


@admin.register(CharBurst)
class CharBurstAdmin(admin.ModelAdmin):
    list_display = ['character']


@admin.register(Move)
class MoveAdmin(admin.ModelAdmin):
    list_display = ['name']
