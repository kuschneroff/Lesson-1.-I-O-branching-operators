'''''Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1'''

import random

n = int(input('Введите натуральное число n, которое определяет кол-во элементов в массиве: '))
x = int(input('Введите начало диапозона массива: '))
y = int(input('Введите конец диапозона массива: '))
my_array = [random.randint(x, y) for i in range(n)]
print(f'Массив {my_array} из {n} элементов')
count = 0
for number in my_array:
    if number == 5:
        count += 1
print(f'Число 5 встречается {count} раз в заданном масcиве от {x} до {y}')