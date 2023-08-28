from django.db import models


class Character(models.Model):
    """
    Character model. All dictionary-like values
    are store within JSON fields.
    """

    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, unique=True)
    weapon = models.CharField(max_length=255)
    element = models.CharField(max_length=255)
    hp = models.JSONField()
    atk = models.JSONField()
    defense = models.JSONField()
    critrate = models.JSONField()
    critdmg = models.JSONField()
    ascension = models.JSONField()
    ascension_stat = models.CharField(max_length=255)
    normal_atk = models.JSONField()
    skill = models.JSONField()
    burst = models.JSONField()
    sprint = models.JSONField(blank=True, null=True)


class Weapon(models.Model):
    """
    Weapon model. All dictionary-like values
    are store within JSON fields.
    """

    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255)
    atk = models.JSONField()
    substat_name = models.CharField(max_length=255, blank=True, null=True)
    substat_lv = models.JSONField(blank=True, null=True)
    passive_stat = models.JSONField(blank=True, null=True)


class Artifact(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, unique=True)
    passive = models.JSONField(blank=True, null=True)
