# Generated by Django 4.2.5 on 2023-09-13 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0004_alter_food_options_alter_types_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='Food_image',
        ),
    ]