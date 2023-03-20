# Иван пришел на рынок и решил купить арбузы: один для себя, второй для тещи.
# Для себя решил выбрать арбуз потяжелее, для тещи полегче.
# Но, арбузов много, непонятко какой тяжелее, какой легче.
# Пользователь вводит число N - количество арбузов. Вторая строка содержит 
# N чисел, записанных на новой строчке каждое. Здесь каждое число это масса 
# соответствующего арбуза. Все числа натруральные и не привышают 30000.

from random import randint

watermelon = int(input('Введите количество арбузов: '))

max_weight, min_weight = 1, 30

for i in range(watermelon):
    next_weight = randint(1, 30)
    print(next_weight, end =' ')
    if next_weight > max_weight:
        max_weight = next_weight
    if next_weight < min_weight:
        min_weight = next_weight

print(f'\nМаксимальный вес {max_weight} для себя, минимальный вес {min_weight} для тещи')