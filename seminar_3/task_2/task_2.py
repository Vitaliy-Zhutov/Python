# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

#Вариант 1
#list_len = int(input('Введите длинну последовательности: '))
#shift = int(input('Введите величину сдевига: '))

#my_list = [_ for _ in range(list_len)]
#print(my_list)

#for i in range(shift):
#    my_list.insert(0, my_list.pop())
#print(my_list)

#Вариант 2
#print(my_list[-shift:] + my_list[:-shift])

#Вариант 3

numb_list = [_ for _ in range(30)]
print(numb_list)
shift = int(input('На сколько сдвигаем: '))

for i in range(len(numb_list)):
    print(numb_list[i - shift], end = ' ')