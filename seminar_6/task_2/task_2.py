# Задача №41. Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 
# 5
# 1 5 1 5 1
# Вывод: 
# 2

from random import randint

# Вариант 1
#print('Введите длинну списка (>3) и диапазон: ')
#my_vars = list(map(int, input('Введите числа через пробел: ').split()))
#my_list1 = [randint(my_vars[1], my_vars[2]) for _ in range(my_vars[0])]
#print(my_list1)
#k = 0
#for i in range(1, my_vars[0] - 1):
#    if my_list1[i-1] < my_list1[i] > my_list1[i+1]:
#        k += 1
#print(k)

# Вариант 2
import random

my_list = [random.randint(1, 10) for _ in range(10)]
print(my_list)
size = len(my_list)

count = 0
for i in range(size):
    if my_list[(i-1) % size] < my_list[i % size] > my_list[(i+1) % size]:
        count +=1

print(f'Таких элементов {count}')