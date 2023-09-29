from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50, unique=True)
    weapon = models.CharField(max_length=20)
    element = models.CharField(max_length=20)
    ascension_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BaseStatModel(models.Model):
    lv1 = models.CharField(max_length=20, null=True)
    lv20 = models.CharField(max_length=20, null=True)
    lv20plus = models.CharField(max_length=20, null=True)
    lv40 = models.CharField(max_length=20, null=True)
    lv40plus = models.CharField(max_length=20, null=True)
    lv50 = models.CharField(max_length=20, null=True)
    lv50plus = models.CharField(max_length=20, null=True)
    lv60 = models.CharField(max_length=20, null=True)
    lv60plus = models.CharField(max_length=20, null=True)
    lv70 = models.CharField(max_length=20, null=True)
    lv70plus = models.CharField(max_length=20, null=True)
    lv80 = models.CharField(max_length=20, null=True)
    lv80plus = models.CharField(max_length=20, null=True)
    lv90 = models.CharField(max_length=20, null=True)

    class Meta:
        abstract = True


class CharHP(BaseStatModel):
    character = models.OneToOneField(
        Character,
        related_name='hp',
        on_delete=models.CASCADE
    )


class CharAtk(BaseStatModel):
    character = models.OneToOneField(
        Character,
        related_name='atk',
        on_delete=models.CASCADE
    )


class CharDef(BaseStatModel):
    character = models.OneToOneField(
        Character,
        related_name='defense',
        on_delete=models.CASCADE
    )


class AscensionStat(BaseStatModel):
    character = models.OneToOneField(
        Character,
        related_name='ascension_stat',
        on_delete=models.CASCADE
    )


class Move(models.Model):
    name = models.CharField(max_length=200)
    lv1 = models.CharField(max_length=30)
    lv2 = models.CharField(max_length=30)
    lv3 = models.CharField(max_length=30)
    lv4 = models.CharField(max_length=30)
    lv5 = models.CharField(max_length=30)
    lv6 = models.CharField(max_length=30)
    lv7 = models.CharField(max_length=30)
    lv8 = models.CharField(max_length=30)
    lv9 = models.CharField(max_length=30)
    lv10 = models.CharField(max_length=30)
    lv11 = models.CharField(max_length=30)
    lv12 = models.CharField(max_length=30)
    lv13 = models.CharField(max_length=30)
    lv14 = models.CharField(max_length=30)
    lv15 = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CharNormAtk(models.Model):
    character = models.ForeignKey(
        Character,
        related_name='normal_atk',
        on_delete=models.CASCADE
    )
    moves = models.ManyToManyField(
        Move
    )

    def __str__(self):
        return self.name


class CharSkill(models.Model):
    character = models.ForeignKey(
        Character,
        related_name='skill',
        on_delete=models.CASCADE
    )
    moves = models.ManyToManyField(
        Move
    )

    def __str__(self):
        return self.name


class CharBurst(models.Model):
    character = models.ForeignKey(
        Character,
        related_name='burst',
        on_delete=models.CASCADE
    )
    moves = models.ManyToManyField(
        Move
    )

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    weapon_type = models.CharField(max_length=500)
    substat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WeaponAtk(BaseStatModel):
    weapon = models.ForeignKey(
        Weapon,
        related_name='atk',
        on_delete=models.CASCADE
    )


class WeaponSub(BaseStatModel):
    weapon = models.ForeignKey(
        Weapon,
        related_name='sub',
        on_delete=models.CASCADE
    )
