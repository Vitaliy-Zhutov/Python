import random

my_list = [i for i in range(1, 21)]
print(my_list)
double_list = my_list.copy()

print(my_list.pop(random.randint(0, 20)))
random.shuffle(my_list)
print(my_list)

for item in double_list:
    if item not in my_list:
        print(item)
        break
