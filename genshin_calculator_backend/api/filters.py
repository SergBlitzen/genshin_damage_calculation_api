from django_filters import rest_framework as filters

from data.models import Character, Weapon


class CalculatorFilter(filters.Filter):
    character_name = filters.CharFilter(method='get_character')
    character_level = filters.CharFilter(method='get_character_level')
    weapon_name = filters.CharFilter(method='get_weapon')
    weapon_level = filters.CharFilter(method='get_weapon_level')
    attack_level = filters.NumberFilter()
    skill_level = filters.NumberFilter()
    burst_level = filters.NumberFilter()

    def get_character(self, value):
        try:
            character = Character.objects.get(shortname=value)
            return character
        except Exception:
            return