# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа 
# сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

sum_number = int(input('Введите количество журавликов: '))

sum_katya = sum_number / 3 * 2
sum_petr = sum_number / 3 / 2
sum_serz = sum_number / 3 / 2

sum_katya = int(sum_katya)
sum_petr = int(sum_petr)
sum_serz = int(sum_serz)

print(f'{sum_petr} {sum_katya} {sum_serz}')
