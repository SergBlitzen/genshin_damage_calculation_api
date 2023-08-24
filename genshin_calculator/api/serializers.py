import json

from rest_framework import serializers

from data.models import Character


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
        read_only_fields = '__all__'

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
