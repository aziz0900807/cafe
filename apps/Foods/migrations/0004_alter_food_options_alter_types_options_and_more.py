# Generated by Django 4.2.5 on 2023-09-12 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0003_alter_subtypes_alpha_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name': 'Блюда', 'verbose_name_plural': ' Блюда'},
        ),
        migrations.AlterModelOptions(
            name='types',
            options={'verbose_name_plural': ' Тип блюда'},
        ),
        migrations.RemoveField(
            model_name='food',
            name='Food_subType',
        ),
        migrations.DeleteModel(
            name='SubTypes',
        ),
    ]
