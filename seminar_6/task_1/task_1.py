# Задача №39. Решение в группах. Даны два массива чисел. 
# Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
# Вывод: 3 3 2 12

import random

print('Необходимо ввести -> 1: Длинна списка 1 2: Длинна списка 2 3: Число мин 4: Число макс')

my_vars = tuple(map(int, input('Введите числа через пробел: ').split()))

my_list1 = [random.randint(my_vars[2], my_vars[3]) for i in range(my_vars[0])]
my_list2 = [random.randint(my_vars[2], my_vars[3]) for i in range(my_vars[1])]

# Вариант 1
my_list3 = [item for item in my_list1 if item not in my_list2]

print(my_list1)
print(my_list2)
print(my_list3)

# Вариант 2
#for item in my_list1:
#    if item not in my_list2:
#        print(item, end=' ')

