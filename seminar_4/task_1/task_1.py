# Задача №25. Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

#input_str = input('Введите произвольные буквы и цифры: ')
#my_list = list(input_str)

#my_dict = dict()
#for item in set(my_list):
#    my_dict.setdefault(item, 0)

#for key, value in my_dict.items():
#    for i in range(len(my_list)):
#        if my_list[i] == key:
#            if value > 0:
#                my_list[i] = f'{key}_{value}'
#            value += 1

#result_str = ''
#for i in my_list:
#    result_str += f'{i}'
#print(result_str)

# Вариант 2
#in_str = input('Введите произвольные буквы и цифры:')
#dict_1 = {'v': '3'}
#for i in in_str:
#    if i in dict_1:
#        print(f'{i}_{dict_1[i]}', end=' ')
#        dict_1[i] += 1
#    else:
#        dict_1[i] = 1
#       print(i, end=' ')

# Вариант 3

import random
import string

my_string = ''.join([random.choice(string.ascii_letters) for _ in range(30)])

dict_count = {}
total_string = ''
for char in my_string:
    dict_count[char] = dict_count.get(char, 0) + 1
    if dict_count.get(char) > 1:
        total_string += f'{char}_{dict_count.get(char)} '
    else:
        total_string += char + ' '
print(total_string)

