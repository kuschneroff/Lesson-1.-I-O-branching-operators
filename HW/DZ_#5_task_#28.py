'''''Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

*Пример:*

2 2
    4 '''''


def summ(x, y):
    if y == 0:
        return x
    elif x == 0:
        return y
    else:
        return summ(x + 1, y - 1)


a, b = map(int, input().split())
print(summ(a, b))