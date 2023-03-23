# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint

# Вариант 1
my_list = [randint(0, 10) for _ in range(5)]
count = 0
for i in range(1, len(my_list)):
    if my_list[i-1] < my_list[i]:
        count += 1
print(my_list)
print(count)

# Вариант 2
new_list = [i for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(my_list)
print(count)

