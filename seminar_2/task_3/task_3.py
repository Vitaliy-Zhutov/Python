# Найти количество теплых дней идущих подряд из рандомного
# списка, от (-3 до 3). Количестово дней вводит
# пользователь.

from random import randint

day = int(input('Введите количество дней: '))

count = 0
count_day = 0
warm_days = 0
temp = randint(-3, 3)

while count <= day:
    temp = temp + randint(-3, 3)
    if temp > 0:
        count_day += 1
    else:
        if warm_days < count_day:
            warm_days = count_day
        count_day = 0
    count += 1
    print(temp, end= ' ')
if warm_days < count_day:
    warm_days = count_day
print()
print(warm_days)
