# Написать программу, которая состоит из 4 этапов:
# - создает список из рандомных четырехзначных чисел
# - принимает с консоли цифру и удаляет ее из всех елементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующие элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# 2 этап: Введите цифру: 3
# 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# 3 этап: [3 1 5 5 3 5 4]
# 4 этап: [3, 1, 5, 4]

import random

my_list = [random.randint(1000, 9999) for _ in range(10)]
print(my_list)

# Этап 2
number = input('Введите число: ')
for i in range(len(my_list)):
    my_list[i] = str(my_list[i]).replace(number, '')
print(my_list)

# Этап 3
# Вариант 1
for i in range(len(my_list)):
    while len(my_list[i]) > 1:
        my_list[i] = str(sum(list(map(int, my_list[i]))))
print(my_list)

# Вариант 2
#for i in range(len(my_list)):
#    while len(my_list[i]) > 1:
#       summa = 0
#       for elem in my_list[i]:
#            summa += int(elem)
#        my_list[i] = str(summa)
#print(my_list)

# Этап 4
print(set(my_list))
