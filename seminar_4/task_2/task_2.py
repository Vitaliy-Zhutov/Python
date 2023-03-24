# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

in_string = input('Введите строку: ').lower()

strings = in_string.split()
set_1 = set()

for i in range(0, len(strings)):
    if strings[i] not in set_1:
        set_1.add(strings[i])

print(set_1)
print('Уникальных слов введено:', len(set_1))

# Вариант 2

import random
import string

my_string = 'Пользователь вводит текст(строка). Словом считается'

for char in string.punctuation:
    my_string = my_string.replace(char, ' ')
my_string = my_string.lower().split()
print(len(set(my_string)))
