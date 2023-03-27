# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

from random import randint
import itertools

num_n = int(input('Введите количество элементов первом в списке n: '))
num_m = int(input('Введите количество элементов во втором списке m: '))

my_list_1 = [randint(1, 10) for _ in range (num_n)]
print(my_list_1)

my_list_2 = [randint(11, 19) for _ in range (num_m)]
print(my_list_2)

result = list(itertools.chain(my_list_1, my_list_2))

result.sort()

print(set(result))
