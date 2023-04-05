# Примеры использования функции map

#num = '123456789'
#num = list(num)
#print(num)

# Вариант подсчета цифр из строки без map
#for i in range(len(num)):
#    num[i] = int(num[i])

# Вариант с map
#num = list(map(int, num))
#print(sum(num))

# Добавляем lambda, приводоим цифры к инту и воводим в степень 2
#num = list(map(lambda x: int(x)**2, num))
#print(num)

#Добавляем функцию filter, находим в списке четные элименты
#num = list(map(int, num))
#num = list(filter(lambda x: x%2 == 0, num))
#print(num)

#Сортировка по индексу 
#import random
#num = [random.randint(0, 100) for _ in range(10)]
#print(num)

# без enumerate
#for i in range(len(num)):
#    if num[i] > 50:
#        print(i)

# с enumerate, с нумерацией от 10
#for i, item in enumerate(num, 10):
#        print(i, item)

# zip функция
import random
num = [random.randint(0, 100) for _ in range(10)]
letters = list('kflgjdhgkd')

print(num)
print(letters)

# без zip

#final = []
#for i in range(len(num)):
#    final.append((num[i], letters[i]))
#print(final)

# с zip

#final = list(zip(num, letters))
#print(final)

# функция lambda

print((lambda x, y, z: x + y + z)(1, 2, 3))








