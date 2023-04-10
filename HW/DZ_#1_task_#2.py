'''Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''

n = int(input('Введите многозначное число: '))
n_str = str(n)
digits_sum = 0
if n < 10:
    print('Попробуй еще разок ввести многозначное число, это точно больше 9')
for i in range(len(n_str)):
    digit = int(n_str[i])
    digits_sum = digits_sum + digit
print(digits_sum)