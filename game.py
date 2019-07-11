#!/usr/bin/env python
# coding: utf-8

# In[2]:


LEGEND = (
    f"На альпийских лугах расплодилось слишком много овец \n"
    f"и они стали представлять угрозу человечеству. \n"
    f"На борьбу с ними призван Волк .\n"
)

HISTORY = (
    f'Действие игры происходит на Альпийских лугах где Волк сражается с кровожадными овцами.\n\n'
    f'Главный герой Волк\n'
    f'Царство: Животные\n'
    f'Тип: Хордовые\n'
    f'Класс: Млекопитающие\n'
    f'Отряд: Хищные\n'
    f'Семейство: Псовые\n\n'
    f'Противники Овцы\n'
    f'Царство: Животные\n'
    f'Тип: Хордовые\n'
    f'Класс: Млекопитающие\n'
    f'Отряд: Парнокопытные\n'
    f'Семейство: Полорогие\n'
    f'Род: 	Бараны\n'
)

HELP = (
    f'Bолк ( может:\n'
    f'Здоровье 300\n'
    f'Кусать за бочок урон -30\n'
    f'Кусать за ногу -15\n'
    f'Царапать  урон - 10\n\n'
    f'Обычная овца\n'
    f'Здровье 100\n'
    f'Кусать урон -5\n'
    f'Бодать волка -15\n\n'
    f'Супер Овца\n'
    f'Здоровье 150\n'
    f'Кусать урон -15\n'
    f'Бодать волка -30\n\n'
    f'Овца безрогая\n'
    f'Здоровье 50\n'
    f'Кусать  -5\n'
    f'Бодать волка -0\n'
)

print(LEGEND)
heroname = input ("Введите имя героя:")
while True:
    herotype = input ("Кто ваш герой Волк(Wolf) или Овца (Sheep):")
    if herotype == 'Wolf':
        Hetoheath = 300
        Attack1 = 30
        Attack2 = 15
        Attack3 =10
        break
    elif hero == 'Sheep':
        print("Ты на темной стороне, перходи на светлую")
    else:
        print("Ты еще не определился?")
print(f'Уууууу, как хорошо, что {herotype} - {heroname} пришел к нам нам на помощь')
while True:
    print(f'Твои команды:\n'
      f'help - помощь\n'
      f'history - история игры\n' 
      f'train - пробное сражение\n'
      f'exit - выход\n'
    )
    action = input()
    if action == 'train':
        print('В Бой!')
        health_sheep = int(input("Прибежала овца, оцени ее здоровье"))
        impact_force = int(input("C какой силой будем бить ее"))
        while health_sheep > 0:
            print(f'У овцы осталось {health_sheep}  здоровья')
            action = input("Ударить овцу yes/no")
            if action == 'yes':
                if (impact_force<health_sheep):
                    health_sheep = health_sheep-health_sheep//4
                else:
                    health_sheep = health_sheep - impact_force
        print('Овца повержена')
    elif action == 'help':
        print(HELP)
    elif action == 'history':
        print(HISTORY)
    elif action == 'exit':
        print(f'Ты, это, заходи, если что')
        break
    else:
        print(f'Неизвестная команда\n')


