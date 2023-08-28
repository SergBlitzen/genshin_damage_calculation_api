import json

from rest_framework import serializers

from data.models import Character, Weapon


class CharacterSerializer(serializers.ModelSerializer):
    """
    Serializer for character objects. Read-only.
    """

    name = serializers.CharField()
    short_name = serializers.CharField()
    weapon = serializers.CharField()
    element = serializers.CharField()
    hp = serializers.SerializerMethodField()
    atk = serializers.SerializerMethodField()
    defense = serializers.SerializerMethodField()
    critrate = serializers.SerializerMethodField()
    critdmg = serializers.SerializerMethodField()
    ascension = serializers.SerializerMethodField()
    ascension_stat = serializers.CharField()
    normal_atk = serializers.SerializerMethodField()
    skill = serializers.SerializerMethodField()
    burst = serializers.SerializerMethodField()
    sprint = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Character
        fields = '__all__'

    # There is no other way to load all attributes from JSON
    # in one method, so for now it's manual.
    def get_hp(self, value):
        data = json.loads(value.hp)
        return data

    def get_atk(self, value):
        data = json.loads(value.atk)
        return data

    def get_defense(self, value):
        data = json.loads(value.defense)
        return data

    def get_critrate(self, value):
        data = json.loads(value.critrate)
        return data

    def get_critdmg(self, value):
        data = json.loads(value.critdmg)
        return data

    def get_ascension(self, value):
        data = json.loads(value.ascension)
        return data

    def get_normal_atk(self, value):
        data = json.loads(value.normal_atk)
        return data

    def get_skill(self, value):
        data = json.loads(value.skill)
        return data

    def get_burst(self, value):
        data = json.loads(value.burst)
        return data

    def get_sprint(self, value):
        if value.sprint:
            data = json.loads(value.sprint)
            return data
        else:
            return None


class WeaponSerializer(serializers.ModelSerializer):
    """
    Serializer for weapon objects. Read-only.
    """

    name = serializers.CharField()
    short_name = serializers.CharField()
    type = serializers.CharField()
    atk = serializers.SerializerMethodField()
    substat_name = serializers.CharField()
    substat_lv = serializers.SerializerMethodField()

    class Meta:
        model = Weapon
        fields = ['name', 'short_name', 'type', 'substat_name', 'atk', 'substat_lv']

    def get_atk(self, value):
        data = json.loads(value.atk)
        return data

    def get_substat_lv(self, value):
        if value.substat_lv:
            data = json.loads(value.substat_lv)
            return data
        else:
            return None


class ElementalDamageSerializer(serializers.Serializer):
    pyro_damage_bonus = serializers.CharField()
    hydro_damage_bonus = serializers.CharField()
    cryo_damage_bonus = serializers.CharField()
    electro_damage_bonus = serializers.CharField()
    geo_damage_bonus = serializers.CharField()
    dendro_damage_bonus = serializers.CharField()
    anemo_damage_bonus = serializers.CharField()
    physical_damage_bonus = serializers.CharField()


class SkillDamageSerializer(serializers.Serializer):
    normal_attack = serializers.JSONField()
    elemental_skill = serializers.JSONField()
    elemental_burst = serializers.JSONField()


class CalculationSerializer(serializers.Serializer):
    character_name = serializers.CharField()
    character_level = serializers.CharField()
    weapon_name = serializers.CharField()
    weapon_level = serializers.CharField()
    hp = serializers.CharField()
    atk = serializers.CharField()
    defense = serializers.CharField()
    elemental_mastery = serializers.CharField()
    energy_recharge = serializers.CharField()
    crit_rate = serializers.CharField()
    crit_damage = serializers.CharField()
    elemental_damage_bonus = ElementalDamageSerializer(many=True)
    skill_damage = SkillDamageSerializer()

