# Generated by Django 4.1.4 on 2023-09-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_weapon_remove_charburst_name_remove_charnormatk_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv70',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv70plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv80',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv80plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv90',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv70',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv70plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv80',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv80plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv90',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv70',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv70plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv80',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv80plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv90',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv70',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv70plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv80',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv80plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv90',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv70',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv70plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv80',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv80plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv90',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv70',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv70plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv80',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv80plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv90',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
