# Generated by Django 4.2.5 on 2023-09-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0012_alter_food_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='types',
            field=models.CharField(choices=[('Салаты', 'Салаты'), ('Супы', 'Супы'), ('Вторые блюда ', 'Вторые блюда '), ('Закускa', 'Закуска'), ('Гарниры', 'Гарниры'), ('Шашлык', 'Iашлык'), ('Пицца', 'Пицца'), ('Мучное', 'Мучное'), ('Десерты', 'Десерты'), ('Чай', 'Чай'), ('Холодные напитки', 'Холодные напитки'), ('Лимонады', 'Лимонады'), ('Молочные коктели', 'Молочные коктели'), ('Виски', 'Виски'), ('разливное пиво', 'разливное пиво'), ('Бутылки пива', 'Бутылки пива'), ('Закуски', 'Закуски'), ('Вино', 'Вино'), ('Коньяк', 'Коньяк'), ('Водка', 'Водка'), ('Текилы', 'Текилы'), ('Ром', 'Ром')], max_length=124, verbose_name='Тип блюда'),
        ),
    ]
