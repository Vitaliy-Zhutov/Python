num = int(input('Введите число: '))
factorial = 1
i = 1 #переменная для вывода в принт num и factorial

while num >= i:
    factorial *= i
    i += 1

print(f'Факториал числа {num} = {factorial}')