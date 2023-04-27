'''''Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''''

import random

n = int(input('Введите кол-во элементов в массива[списке]: '))
x = int(input('Начало диапазона: '))
y = int(input('Конец диапазона: '))
my_array = [random.randint(x, y) for i in range(n)]
print(my_array)
min_val = int(input('Введи минимум: '))
max_val = int(input('Введи максимум: '))
for i in range(len(my_array)):
    if min_val <= my_array[i] <= max_val:
        print([i])
