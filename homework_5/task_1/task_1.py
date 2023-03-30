# Задача 26:  Напишите программу, которая на вход принимает два числа
# A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

numb_a = int(input('Введите число А: '))
numb_b = int(input('Введите число B: '))

def degree_numb (numb_a, numb_b):
    if numb_b == 0:
        return 1
    return numb_a * degree_numb(numb_a, numb_b - 1)

print(degree_numb(numb_a, numb_b))