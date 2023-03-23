# Найти количество уникальных элементов в рандомном списке

import random

numb_list = [random.randint(0, 20) for _ in range (30)]

print(numb_list)

numb_set = set(numb_list) # формируем множество
print(numb_set)           # получаем упорядоченный список множества
print(len(numb_set))      # считаем количетво элементов