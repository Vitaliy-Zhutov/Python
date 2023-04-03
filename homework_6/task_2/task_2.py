# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

num_list = int(input('Введите размер списка(массива): '))

my_list = [randint(1, 10) for _ in range (num_list)]
print(my_list)

min_number = int(input('Введите минимальное значение (от 1 до 10) min: '))
max_number = int(input('Введите максимальное значение (от 1 до 10) max: '))

for i in range(len(my_list)):
  if min_number <= my_list[i] <= max_number:
    print(i, end=' ')
