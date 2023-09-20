from django.db import models

class Food(models.Model):
    type=(
        ('Салаты','Салаты'),
        ('Супы','Супы'),
        ('Вторые блюда ','Вторые блюда '),
        ('Закускa','Закуска'),
        ('Гарниры','Гарниры'),
        ('Шашлык','Шашлык'),
        ('Пицца','Пицца'),
        ('Мучное','Мучное'),
        ('Десерты','Десерты'),
        ('Чай','Чай'),
        ('Холодные напитки','Холодные напитки'),
        ('Лимонады','Лимонады'),
        ('Молочные коктели','Молочные коктели'),
        ('Виски','Виски'),
        ('Разливное пиво','Разливное пиво'),
        ('Бутылочное пива','Бутылочное пива'),
        ('Закуски','Закуски'),
        ('Вино','Вино'),
        ('Коньяк','Коньяк'),
        ('Водка','Водка'),
        ('Текилы','Текилы'),
        ('Ром','Ром'),
        ('Ликеры','Ликеры'),
    )
    Food_name = models.CharField(max_length=64,verbose_name="Название блюда")

    types=models.CharField(max_length=124,verbose_name='Тип блюда',choices=type)
    Food_price = models.IntegerField(verbose_name="Цена блюда")
    food_menu = models.CharField(max_length=124,verbose_name='тип меню',choices=(('бар','бар'),('кафе','кафе')))
    def __str__(self):
        return self.Food_name[:15]
    
    class Meta:
        verbose_name="Блюда"
        verbose_name_plural=" Блюда"
