# Generated by Django 4.1.4 on 2023-09-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_alter_ascensionstat_lv70_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv20',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv20plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv40',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv40plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv50',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv50plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv60',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ascensionstat',
            name='lv60plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv20',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv20plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv40',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv40plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv50',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv50plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv60',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charatk',
            name='lv60plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv20',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv20plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv40',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv40plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv50',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv50plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv60',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chardef',
            name='lv60plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv20',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv20plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv40',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv40plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv50',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv50plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv60',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='charhp',
            name='lv60plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv20',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv20plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv40',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv40plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv50',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv50plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv60',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponatk',
            name='lv60plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv20',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv20plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv40',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv40plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv50',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv50plus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv60',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='weaponsub',
            name='lv60plus',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
