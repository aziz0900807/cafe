from django.shortcuts import render,redirect
from apps.Foods.models import Food
# Create your views here.
def index(request):
    food=Food.objects.in_bulk()
    m_food=[]
    b_food=[]
    menu=["Салаты",'Супы','Вторые блюда ','Закуска','Гарниры'
          ,'Шашлык','Пицца','Мучное','Десерты','Чай','Холодные напитки']
    
    bar=['Лимонады','Молочные коктели','Виски','Разливное пиво','Бутылочное пива',"Ликеры"
         ,'Закуски','Вино','Коньяк','Водка','Текилы','Ром']
    
    for i in food:
        if food[i].types in menu:
            m_food.append(food[i])
        if food[i].types in bar:
            b_food.append(food[i])
    index=0
    context={'Menu':m_food,'Bar':b_food,"Type_menu":menu,"Type_bar":bar,"index":index}
    return render(request,'index.html',context)
