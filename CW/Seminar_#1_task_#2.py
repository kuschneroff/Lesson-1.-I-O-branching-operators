#В некоторой школе решили набрать три новых математических класса и оборудовать
#кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов.
#Выведите наименьшее число парт, которое нужно приобрести для них.

group_one = int(input('Введите кол-во детей в классе 1"А": '))
group_two = int(input('Введите кол-во детей в классе 1"Б": '))
group_three = int(input('Введите кол-во детей в классе 1"В": '))
total_table_one = group_one // 2 + group_one % 2
total_table_two = group_two // 2 + group_two % 2
total_table_three = group_three // 2 + group_three % 2
print(f'Получается,что в классе 1"А" {group_one} детей и потребуется {total_table_one} парт в кабинете')
print(f'Получается,что в классе 1"Б" {group_two} детей и потребуется {total_table_two} парт в кабинете')
print(f'Получается,что в классе 1"В" {group_three} детей и потребуется {total_table_three} парт в кабинете')
print(f'Наименьшее число парт {total_table_one + total_table_two + total_table_three}, которое нужно приобрести для них')