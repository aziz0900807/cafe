# Generated by Django 4.2.5 on 2023-09-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0009_alter_food_food_type_alter_types_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='Food_type',
        ),
        migrations.AddField(
            model_name='food',
            name='types',
            field=models.CharField(default=1, max_length=124, verbose_name='Тип блюда'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Types',
        ),
    ]
