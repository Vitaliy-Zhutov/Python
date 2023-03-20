# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

num_user = int(input('Введите целое число: '))

degree = 0

while 2 ** degree <= num_user:
    result = 2 ** degree
    degree += 1
    print(result)
