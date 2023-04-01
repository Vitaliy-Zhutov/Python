# Задача №45.Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10**5. Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 300
# Вывод: 220 284

dict_divisors = {}

def divisors(number: int) -> int:
    divisor_list = []
    for div in range(1, number // 2 + 1):
        if not number % div:
            divisor_list.append(div)
    return sum(divisor_list)

for number in range(5000):
    dict_divisors[number] = divisors(number)

list_pair = []
for key, value in dict_divisors.items():
    if dict_divisors.get(dict_divisors.get(key)) == key and key != value:
        if(value, key) not in list_pair:
            list_pair.append((key, value))
            print((key, value))