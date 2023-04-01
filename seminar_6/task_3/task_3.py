# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.
# Ввод: 1 2 3 2 3 
# Вывод: 2

from random import randint

print('Введите длинну списка (>3) и диапазон')
my_vars = list(map(int, input('Введите числа через пробел: ').split()))
my_list = [randint(my_vars[1], my_vars[2]) for _ in range(my_vars[0])]
print(my_list)

dict = {}
for i in my_list:
    dict[i] = dict.get(i, 0) + 1

sum = 0
for key, value in dict.items():
    sum += value // 2

print(f'Таких пар в списке: {sum}')

# Вариант 2
#import random

#my_list = [random.randint(0, 10) for _ in range(10)]
#print(my_list)

#count = 0
#for item in range(11):
#    count += my_list.count(item)//2

#print(count)
