# Generated by Django 4.2.5 on 2023-09-12 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0002_subtypes_alpha_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtypes',
            name='alpha_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_types', to='Foods.types', verbose_name='Тип'),
        ),
    ]
