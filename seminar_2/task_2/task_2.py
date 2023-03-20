# Дано натуральное чило A > 1. Определите каким по счету
# числом Фибоначчи оно является. Выведите такое число n,
# что Ф(n)=А. Если А не является числом Фибоначчи, выодим -1

num = int(input('Введите число для проверки: '))
fib_n_1 = 1
fib_n_2 = 0
fib = 1
index = 2
while fib < num:
    fib = fib_n_1 + fib_n_2
    fib_n_2 = fib_n_1
    fib_n_1 = fib
    index += 1
    print('fib =', fib)

if fib_n_1 == num:
    print('The number is fibonachi number, index =', index)
else:
    print('-1')
