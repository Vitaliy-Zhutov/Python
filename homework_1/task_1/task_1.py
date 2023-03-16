# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

initial_number = int(input('Введите трехзначное число: '))

num1 = initial_number // 100 
num2 = initial_number // 10 % 10
num3 = initial_number % 10 
sum = num1 + num2 + num3

print(sum)
