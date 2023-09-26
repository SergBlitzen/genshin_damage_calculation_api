from django.db import models


class BaseStatModel(models.Model):
    lv1 = models.CharField(max_length=20)
    lv20 = models.CharField(max_length=20)
    lv20plus = models.CharField(max_length=20)
    lv40 = models.CharField(max_length=20)
    lv40plus = models.CharField(max_length=20)
    lv50 = models.CharField(max_length=20)
    lv50plus = models.CharField(max_length=20)
    lv60 = models.CharField(max_length=20)
    lv60plus = models.CharField(max_length=20)
    lv70 = models.CharField(max_length=20)
    lv70plus = models.CharField(max_length=20)
    lv80 = models.CharField(max_length=20)
    lv80plus = models.CharField(max_length=20)
    lv90 = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Character(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    weapon = models.CharField(max_length=20)
    element = models.CharField(max_length=20)
    ascension_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


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


class CharCritDMG(BaseStatModel):
    character = models.OneToOneField(
        Character,
        related_name='crit_dmg',
        on_delete=models.CASCADE
    )


class CharCritRate(BaseStatModel):
    character = models.OneToOneField(
        Character,
        related_name='crit_rate',
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
    name = models.CharField(max_length=200)
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
    name = models.CharField(max_length=200)
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
    name = models.CharField(max_length=200)
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
